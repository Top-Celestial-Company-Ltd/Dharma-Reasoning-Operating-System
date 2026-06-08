"""
DROS 7.3 Graphify v2.6 - 剛柔並濟語義圖譜檢索引擎 (數位佛堂增強快取相容版)
目標：融合 v1.0 的嚴格目錄排除、v2.0 的多維度權重排序與標籤提取，以及本地開發環境專用的 pickle 快取效能防禦
"""

import re
import time
import sys
import logging
import os
import pickle
from pathlib import Path
from collections import defaultdict
from typing import List, Dict, Optional, Tuple

from src.config import config

logger = logging.getLogger("DROS.Graphify")


class GraphifyRetriever:
    """Graphify v2.6 核心相容暨大覺藏座標直連增強型檢索引擎 (含高效率 Pickle 快取防禦)"""
    
    def __init__(self, core_path: Optional[Path] = None):
        self.core_path = Path(core_path or config.core_path)
        self.cache_path = self.core_path.parent / ".graphify_cache.pkl"
        
        # 效能防禦：使用 pickle 快取
        loaded_from_cache = False
        
        try:
            files = list(self.core_path.rglob("*.md"))
            if files:
                current_max_mtime = max(os.path.getmtime(f) for f in files)
                current_file_count = len(files)
            else:
                current_max_mtime = 0
                current_file_count = 0
                
            if self.cache_path.exists():
                with open(self.cache_path, "rb") as f:
                    cache_data = pickle.load(f)
                
                # 額外檢查 "t_coordinates" 欄位，確保載入的快取是完整的 v2.6 格式
                if (cache_data.get("max_mtime") == current_max_mtime and 
                    cache_data.get("file_count") == current_file_count and
                    "index" in cache_data and
                    "t_coordinates" in cache_data["index"]):
                    self.index = cache_data["index"]
                    loaded_from_cache = True
                    logger.info(f"⚡ [Graphify] 成功從 Pickle 快取載入索引，共 {len(self.index['nodes'])} 個節點 (耗時微秒級)")
            
            if not loaded_from_cache:
                logger.info("⏳ [Graphify] 快取失效或不存在，正在重新建立增強型索引...")
                self.index = self._build_graph_index()
                # 寫入快取
                cache_data = {
                    "index": self.index,
                    "max_mtime": current_max_mtime,
                    "file_count": current_file_count
                }
                with open(self.cache_path, "wb") as f:
                    pickle.dump(cache_data, f)
                logger.info(f"💾 [Graphify] 增強型索引建立並已序列化保存，共 {len(self.index['nodes'])} 個節點")
        except Exception as e:
            logger.warning(f"⚠️ [Graphify] 快取處理異常，降級為無快取模式: {e}")
            self.index = self._build_graph_index()

    def _build_graph_index(self) -> Dict:
        """建立增強型記憶體圖譜索引 (融合 v1.0 的嚴格目錄排除，杜絕重複源污染，內建效能監控)"""
        start_time = time.perf_counter()
        logger.info("正在建立 Graphify v2.6 索引...")
        
        index = {
            "nodes": {},           # node_name_lower -> file_path
            "keywords": defaultdict(list),  # keyword -> [node_names]
            "t_coordinates": defaultdict(list),  # t_id_lower -> [node_names] (O(1) 座標直接映射表)
            "cross_refs": defaultdict(set)  # 拓撲關聯
        }

        # 嚴格排除目錄名單 (全小寫)
        EXCLUDE_DIRS = {
            "long_classics", 
            "system_docs", 
            "pavilion_sandbox", 
            "pavilion_digital", 
            "user_pavilion",
            "backups",
            "backup",
            "tempbackupcheck",
            "temp_refine",
            "temp_refine_single",
            "temp_run"
        }

        for md_file in self.core_path.rglob("*.md"):
            # 取得相對於 core_path 的父目錄名稱，進行小寫比對過濾
            relative_parts = [p.lower() for p in md_file.relative_to(self.core_path).parts[:-1]]
            
            should_exclude = False
            for part in relative_parts:
                if (part in EXCLUDE_DIRS or 
                    "backup" in part or 
                    "temp" in part or 
                    "sandbox" in part or 
                    "pavilion" in part or
                    "long_classics" in part or
                    "system_docs" in part):
                    should_exclude = True
                    break
            
            if should_exclude:
                continue

            node_name = md_file.stem
            index["nodes"][node_name.lower()] = md_file

            try:
                # 1. 優先提取節點名稱本身的 N-Gram（極致高保真義理名相，100% 無雜音）
                name_ngrams = self._extract_ngrams(node_name)
                for ngram in name_ngrams:
                    index["keywords"][ngram].append(node_name)

                # 2. 僅讀取前 300 字（核心義理摘要），相較 3000 字降低 90% 以上的記憶體與啟動效能負擔
                content = md_file.read_text(encoding='utf-8')[:300]
                
                # 提取摘要中的中文 N-Gram
                content_ngrams = self._extract_ngrams(content)
                for ngram in content_ngrams:
                    index["keywords"][ngram].append(node_name)
                
                # 3. 提取括號內的重要標註（如 [!NOTE]、[!QUOTE] 後的關鍵詞）
                tags = re.findall(r'\[\!.*?\](.*?)[\n\r]', content)
                for tag in tags:
                    tag_ngrams = self._extract_ngrams(tag)
                    for ngram in tag_ngrams:
                        index["keywords"][ngram].append(node_name)

                # 4. 提取 T-編號 真理座標，建立 O(1) 座標對齊索引表
                t_ids = re.findall(r'T\d{4}[a-zA-Z]?', content)
                for t_id in t_ids:
                    index["t_coordinates"][t_id.lower()].append(node_name)
                        
            except Exception:
                continue

        duration = time.perf_counter() - start_time
        
        # 估算索引大略記憶體開銷 (字典結構本身 + key-value 估算)
        keywords_est_bytes = sys.getsizeof(index["keywords"]) + sum(sys.getsizeof(k) + sys.getsizeof(v) for k, v in index["keywords"].items())
        t_coords_est_bytes = sys.getsizeof(index["t_coordinates"]) + sum(sys.getsizeof(k) + sys.getsizeof(v) for k, v in index["t_coordinates"].items())

        logger.info(
            f"Graphify v2.6 索引建立完成 | 耗時: {duration:.4f} 秒 | "
            f"實際掛載節點: {len(index['nodes'])} | "
            f"關鍵詞索引: {len(index['keywords'])} (估計: {keywords_est_bytes / 1024:.2f} KB) | "
            f"座標索引: {len(index['t_coordinates'])} (估計: {t_coords_est_bytes / 1024:.2f} KB)"
        )

        return index

    # 常用口語虛詞與無意義詞過濾表 (保護記憶體與啟動效能，根治分詞雜音)
    STOP_WORDS = {
        "我們", "可以", "因為", "所以", "但是", "一個", "因此", "這個", "這些", "以及", 
        "而且", "如果", "沒有", "進行", "開始", "目前", "特別", "對於", "關於", "什麼",
        "這樣", "那樣", "這時", "那時", "由於", "就是", "也是", "有些", "其中", "不是",
        "那麼", "或者", "或是", "並且", "然後", "已經", "正在", "非常", "相當", "比較",
        "如何", "為何", "什麼時候", "哪裡", "因此", "因為", "所以", "並且", "可以", "有些"
    }

    def _extract_ngrams(self, text: str, min_len: int = 2, max_len: int = 4) -> List[str]:
        """高效率提取中文字元的 2~4 字 N-Gram（內建停用詞過濾）"""
        chinese_blocks = re.findall(r'[\u4e00-\u9fa5]+', text)
        ngrams = []
        for block in chinese_blocks:
            n = len(block)
            for length in range(min_len, min(max_len + 1, n + 1)):
                for i in range(n - length + 1):
                    word = block[i:i+length]
                    if word not in self.STOP_WORDS:
                        ngrams.append(word)
        return list(set(ngrams))

    def search(self, query: str, top_k: int = 10, min_score: float = 6.0, sectarian_context: str = "通用", user_query: str = "") -> List[Dict]:
        """v2.7 強化檢索：極速座標匹配 + 多維度權重 + N-Gram 語義擴展 + 倒排匹配 + 宗派標籤過濾"""
        start_time = time.perf_counter()
        if not query or not query.strip():
            return []

        query_lower = query.lower().strip()
        score_dict = defaultdict(float)

        # 0. 座標精準匹配（O(1) 精準查表）
        query_t_ids = re.findall(r'[tT]\d{4}[a-zA-Z]?', query_lower)
        for q_t_id in query_t_ids:
            if q_t_id in self.index.get("t_coordinates", {}):
                for node_name in self.index["t_coordinates"][q_t_id]:
                    score_dict[node_name.lower()] += 40.0  # 提供超高的極致優先級

        # 1. 精準名稱匹配（最高權重）
        if query_lower in self.index["nodes"]:
            score_dict[query_lower] += 35

        # 提取查詢字句的 N-Gram
        query_ngrams = self._extract_ngrams(query)

        # 2. 關鍵詞 N-Gram 匹配
        for ngram in query_ngrams:
            if ngram in self.index["keywords"]:
                weight = len(ngram) * 4.5  # 2字=9分，3字=13.5分，4字=18分
                for node_name in self.index["keywords"][ngram]:
                    score_dict[node_name.lower()] += weight

        # 3. 模糊匹配與部分匹配
        for node_name in self.index["nodes"]:
            name_lower = node_name.lower()
            if query_lower in name_lower:
                score_dict[name_lower] += 22
            elif any(w in name_lower for w in query_ngrams):
                score_dict[name_lower] += 9

        # 排序並過濾
        sorted_results = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)
        
        results = []
        for node_name, score in sorted_results[:top_k]:
            if score >= min_score:
                node = self._load_node_detail(node_name, user_query or query, sectarian_context)
                if node:
                    node["match_score"] = round(score, 1)
                    results.append(node)

        duration = time.perf_counter() - start_time
        logger.info(f"Graphify 檢索完成 | 查詢: '{query}' | 宗派: '{sectarian_context}' | 耗時: {duration * 1000:.2f} 毫秒 | 回傳結果數: {len(results)}")
        return results

    def _load_node_detail(self, node_name: str, query: str = "", sectarian_context: str = "通用") -> Optional[Dict]:
        """載入節點詳細內容，若掛載大覺藏則動態加載與檢索詞最契合的原始經文段落 (支援宗派過濾與配額熔斷)"""
        path = self.index["nodes"].get(node_name.lower())
        if not path:
            return None

        try:
            content = path.read_text(encoding='utf-8')
            
            summary = re.search(r"> \[!NOTE\].*?(?:\n>.*)+", content, re.S)
            quote_match = re.search(r"> \[!QUOTE\].*?(?:\n>.*)+", content, re.S)

            summary_text = summary.group(0) if summary else ""
            quote_text = quote_match.group(0) if quote_match else ""

            # 若有啟用大覺藏且存在 T-座標，進行動態引文載入與精準切片
            vault_path = Path(config.vault_path)
            if vault_path.exists():
                t_ids = list(set(re.findall(r'T\d{4}[a-zA-Z]?', summary_text or content)))
                if t_ids:
                    dynamic_quotes = []
                    query_terms = self._extract_ngrams(query) if query else []
                    
                    # 引入配額控制計數器
                    quote_count = 0
                    max_slices = getattr(config, 'max_quote_slices', 3)
                    
                    for t_id in t_ids:
                        if quote_count < max_slices:
                            classic_file = self._find_classic_file(vault_path, t_id, sectarian_context)
                            if classic_file and classic_file.exists():
                                segment = self._extract_relevant_segment(classic_file, query_terms)
                                if segment:
                                    # 安全消毒與清洗
                                    sanitized_segment = self._sanitize_content(segment)
                                    dynamic_quotes.append(
                                        f"> [!QUOTE] 【大覺藏原典動態載入 ({t_id})】\n" + 
                                        "\n".join(f"> {line}" for line in sanitized_segment.split("\n"))
                                    )
                                    quote_count += 1
                                else:
                                    logger.warning(f"大覺藏原典切片失敗 | 檔案: {classic_file} | 座標: {t_id}")
                                    dynamic_quotes.append(
                                        f"> [!WARNING] 【大覺藏加載降級 ({t_id})】\n" +
                                        f"> *真理座標對應之經文段落切片失敗，已啟用安全降級守衛。*"
                                    )
                            elif classic_file is None and sectarian_context != "通用":
                                # 被宗派隔離阻斷，不計入 quote_count，寫入提示
                                dynamic_quotes.append(
                                    f"> [!WARNING] 【大覺藏加載隔離 ({t_id})】\n" +
                                    f"> *此座標非隸屬當前宗派「{sectarian_context}」物理目錄，已依義理隔離契約物理阻斷。*"
                                )
                            else:
                                logger.warning(f"找不到大覺藏原典檔案 | 座標: {t_id} | 路徑: {vault_path}")
                                dynamic_quotes.append(
                                    f"> [!WARNING] 【大覺藏加載降級 ({t_id})】\n" +
                                    f"> *大覺藏庫中查無與座標 {t_id} 匹配之經典檔案，已啟用安全降級守衛。*"
                                )
                        else:
                            # 超限，進入安全折疊模式，扼殺 400 錯誤
                            dynamic_quotes.append(
                                f"> [!NOTE] 【大覺藏加載折疊 ({t_id})】\n" +
                                f"> *[T-Number: {t_id} (因 Token 預算限制已折疊，請手動定錨此座標)]*"
                            )
                    
                    if dynamic_quotes:
                        # 將動態載入的原典內容拼接到原有 quote_text 後方
                        dynamic_block = "\n\n".join(dynamic_quotes)
                        if quote_text:
                            quote_text += f"\n\n{dynamic_block}"
                        else:
                            quote_text = dynamic_block

            return {
                "name": path.stem,
                "path": str(path),
                "summary": summary_text,
                "quote": quote_text,
                "has_authority": bool(quote_text)
            }
        except Exception as e:
            logger.warning(f"載入節點失敗 {node_name}: {e}")
            return None

    def _find_classic_file(self, vault_path: Path, t_id: str, sectarian_context: str = "通用") -> Optional[Path]:
        """在大覺藏庫中尋找與 T-編號 匹配的經文檔案，並基於宗派進行物理子目錄過濾"""
        try:
            t_id_clean = t_id.upper()
            
            # 建立標籤與大覺藏物理目錄的映射字典 (支援 Windows 與 Posix 路徑分隔符)
            PATH_MAPPING = {
                "唯識宗": ["01-大正藏/14瑜伽部類/", "07-瑜伽師地論/"],
                "中觀派": ["01-大正藏/13中觀部類/", "01-大正藏/03般若部類/"],
                "天台宗": ["01-大正藏/04法華部類/", "12-智師/"],
                "阿毗達摩": ["01-大正藏/12毘曇部類/"],
                "原始阿含": ["01-大正藏/01阿含部類/"],
                "華嚴唯心": ["01-大正藏/05華嚴部類/"],
                "如來藏/真常派": ["01-大正藏/06寶積部類/", "01-大正藏/07涅槃部類/", "01-大正藏/10密教部類/"]
            }
            
            sub_dirs = PATH_MAPPING.get(sectarian_context, [])
            
            # 優先在宗派限定目錄下搜尋
            if sub_dirs:
                for sub_dir in sub_dirs:
                    target_path = vault_path / sub_dir
                    if target_path.exists():
                        for p in target_path.rglob(f"*{t_id_clean}*.md"):
                            logger.info(f"🎯 [Graphify] 宗派過濾匹配成功 ({sectarian_context}): '{p.name}'")
                            return p
                # 若限制了宗派但在對應目錄下找不到，則基於「嚴格宗派物理隔離」原則返回 None，防止污染
                logger.info(f"🚫 [Graphify] 宗派限制 ({sectarian_context}) 阻斷座標 '{t_id_clean}' 之跨館越界打撈")
                return None
            
            # 通用模式：掃描全庫
            for p in vault_path.rglob(f"*{t_id_clean}*.md"):
                return p
        except Exception:
            pass
        return None

    def _extract_relevant_segment(self, file_path: Path, query_terms: List[str], max_chars: int = 800) -> str:
        """從原始經典中提取與關鍵字最相關的段落切片"""
        try:
            content = file_path.read_text(encoding='utf-8')
            # 移除 Front matter (開頭 YAML)
            content_clean = re.sub(r'^---.*?\n---\n', '', content, flags=re.S).strip()
            
            # 切分成段落
            paragraphs = [p.strip() for p in re.split(r'\n+', content_clean) if p.strip()]
            
            # 尋找匹配字數最多的段落
            best_para = None
            best_score = 0
            for para in paragraphs:
                # 避開標題與註解
                if para.startswith("---") or para.startswith("#"):
                    continue
                
                score = 0
                for term in query_terms:
                    if len(term) >= 2 and term in para:
                        score += len(term)
                
                if score > best_score:
                    best_score = score
                    best_para = para
            
            # 如果找到了包含關鍵字的段落，返回該段落以及前後的上下文（不超過 max_chars）
            if best_para:
                best_idx = paragraphs.index(best_para)
                selected = []
                
                # 向前看一段
                if best_idx > 0 and not paragraphs[best_idx-1].startswith("#"):
                    selected.append(paragraphs[best_idx-1])
                    
                selected.append(best_para)
                
                # 向後看一段
                if best_idx < len(paragraphs) - 1:
                    selected.append(paragraphs[best_idx+1])
                    
                segment = "\n\n".join(selected)
                if len(segment) > max_chars:
                    segment = segment[:max_chars] + "..."
                return segment
                
            # 若無匹配段落，則回退加載前 800 字
            if len(content_clean) > max_chars:
                return content_clean[:max_chars] + "..."
            return content_clean
        except Exception as e:
            return f"【大覺藏加載錯誤：{e}】"

    def _sanitize_content(self, text: str) -> str:
        """安全防禦：消毒並清洗經文段落內容，防止自訂 Vault 惡意注入或惡意標籤"""
        if not text:
            return ""
        # 1. 移除潛在的 HTML 標籤（如 <script>, <iframe> 等），防止前端注入渲染
        cleaned = re.sub(r'<[^>]+>', '', text)
        
        # 2. 過濾惡意的 Prompt Injection 注入特徵字句（如 'ignore previous', 'system prompt bypass' 等）
        cleaned = re.sub(
            r'(?i)(ignore\s+previous|system\s+prompt|bypass\s+instructions|忽略先前|繞過系統|你是\s*LLM)', 
            '[已安全消毒之異常指令]', 
            cleaned
        )
        
        # 3. 避免 markdown 連結中的 javascript: 協議等漏洞，防止 Markdown 渲染器攻擊
        cleaned = re.sub(r'\[([^\]]*)\]\(javascript:[^\)]*\)', r'[\1](#)', cleaned)
        
        return cleaned.strip()


# ====================== 便捷函數 ======================
def get_retriever() -> GraphifyRetriever:
    """全域便捷取得檢索器"""
    return GraphifyRetriever()

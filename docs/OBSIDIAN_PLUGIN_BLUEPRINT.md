# 🔌 DROS Doctrinal Copilot - Obsidian Plugin Development Blueprint

## Building the Ultimate Local "Tripitaka Doctrinal Companion" Plugin

[繁體中文](OBSIDIAN_PLUGIN_BLUEPRINT_zh.md) | [English](OBSIDIAN_PLUGIN_BLUEPRINT.md)

> **"Simplicity is the ultimate sophistication. By empowering the Obsidian ecosystem, DROS brings sovereign reasoning straight to the practitioner's fingertips."**  
> ── Top Celestial Company Ltd. / Jimmy Chen

This blueprint provides the complete architectural design, core TypeScript interfaces, Svelte sidebar component styling, and a two-stage development roadmap (from local API bridging to a zero-dependency local WASM engine) for the official **DROS Doctrinal Copilot** Obsidian plugin.

---

## 🏛️ 1. Directory Structure

A standard DROS Obsidian plugin directory contains the following files:

```text
dros-copilot/
├── manifest.json         # Plugin manifest (name, version, dependencies)
├── styles.css            # Dark Zen and Glassmorphism stylesheet
├── main.ts               # Plugin entry (registers Ribbon button, hotkeys, sidebar view)
└── ChatPanel.svelte      # Svelte-based chat panel and card preview interface
```

### 1. manifest.json
```json
{
  "id": "dros-doctrinal-copilot",
  "name": "DROS Doctrinal Copilot",
  "version": "1.0.0",
  "minAppVersion": "1.0.0",
  "description": "Dharma Reasoning OS local companion and doctrinal anchoring Copilot. Provides Vajra/Bodhisattva dual-contract reasoning, one-click synaptic bi-directional linking, and doctrinal card anchoring.",
  "author": "Top Celestial Company Ltd. / Jimmy Chen",
  "authorUrl": "https://github.com/JimmyChen-KC",
  "isDesktopOnly": false
}
```

---

## ⚡ 2. Stage 1: Local Proxy Bridge (Fastest MVP)

In Stage 1, the plugin acts as a frontend GUI that calls the local FastAPI backend `gemini_proxy.py` (which runs in the background using approx. 100MB of RAM).

```
[ Obsidian UI Panel ] ───(HTTP fetch/stream)───> [ http://127.0.0.1:8080/v1/chat/completions ]
        │                                                     │
        ▼                                                     ▼
[ Select text Alt+D ] ───────────────────────────────────> [ Query 16,347 in-memory dict ]
```

### 1. main.ts
```typescript
import { Plugin, WorkspaceLeaf, ItemView, Notice, requestUrl } from 'obsidian';

const VIEW_TYPE_DROS_CHAT = "dros-chat-view";

class DrosChatView extends ItemView {
    constructor(leaf: WorkspaceLeaf) {
        super(leaf);
    }

    getViewType() { return VIEW_TYPE_DROS_CHAT; }
    getDisplayText() { return "DROS Doctrinal Copilot"; }
    getIcon() { return "dharmachakra"; } // Custom wheel icon

    async onOpen() {
        const container = this.containerEl.children[1];
        container.empty();
        container.createEl("h3", { text: "🪷 DROS Copilot Panel" });
        
        const chatContainer = container.createDiv({ cls: "dros-chat-container" });
        // new ChatPanel({ target: chatContainer });
    }
}

export default class DrosCopilotPlugin extends Plugin {
    async onload() {
        console.log('DROS Doctrinal Copilot successfully loaded! 🪷');

        this.registerView(VIEW_TYPE_DROS_CHAT, (leaf) => new DrosChatView(leaf));

        this.addRibbonIcon('dharmachakra', 'Start DROS Companion', () => {
            this.activateView();
        });

        // Register hotkey Alt + D for local card anchoring and query
        this.addCommand({
            id: 'dros-quick-lookup',
            name: 'DROS: Local Doctrinal Anchoring & Query',
            hotkeys: [{ modifiers: ["Alt"], key: "d" }],
            editorCallback: async (editor, view) => {
                const selectedText = editor.getSelection().trim();
                if (!selectedText) {
                    new Notice('Please select the doctrinal term you wish to anchor first!');
                    return;
                }

                new Notice(`🔍 Querying DROS anchoring for: ${selectedText}...`);

                try {
                    const response = await requestUrl({
                        url: 'http://127.0.0.1:8080/v1/chat/completions',
                        method: 'POST',
                        contentType: 'application/json',
                        body: JSON.stringify({ query: selectedText })
                    });

                    // Anchor the selected text into [[Concept]] format
                    editor.replaceSelection(`[[${selectedText}]]`);
                    
                    new Notice(`【DROS Doctrinal Anchoring Success】\n${response.json.reply}`);
                } catch (err) {
                    new Notice('❌ DROS Local Proxy not running. Please launch "gemini_proxy.py"!');
                }
            }
        });
    }

    async activateView() {
        this.app.workspace.detachLeavesOfType(VIEW_TYPE_DROS_CHAT);
        await this.app.workspace.getRightLeaf(false).setViewState({
            type: VIEW_TYPE_DROS_CHAT,
            active: true,
        });
        this.app.workspace.revealLeaf(
            this.app.workspace.getLeavesOfType(VIEW_TYPE_DROS_CHAT)[0]
        );
    }
}
```

---

## 🎨 3. Zen and Glassmorphic UI Design (Styles & Svelte CSS)

To invoke a "digital temple" atmosphere, the interface features **dark Zen styling, Glassmorphism, and gold/jade halos**:

```css
/* styles.css */
.dros-chat-container {
    background: rgba(30, 30, 30, 0.65) !important;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 215, 0, 0.15); /* Vajra Gold Border */
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    color: #e0e0e0;
}

/* Bodhisattva Mode Toggle Button */
.dros-route-switch {
    background: linear-gradient(135deg, rgba(0, 128, 128, 0.2), rgba(255, 215, 0, 0.2));
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    padding: 8px 12px;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.dros-route-switch:hover {
    box-shadow: 0 0 15px rgba(255, 215, 0, 0.4);
    transform: translateY(-1px);
}

/* Dharma Card (Doctrinal Card) */
.dros-dharma-card {
    background: rgba(255, 255, 255, 0.05);
    border-left: 3px solid #ffd700; /* Vajra Gold Line */
    border-radius: 4px;
    padding: 10px;
    margin: 8px 0;
    font-size: 0.9em;
}
```

---

## 🕸️ 4. Stage 2: Zero-Ops Local TS/WASM Engine (No-Python)

To enable zero-configuration for general users, Stage 2 migrates DROS topological routing directly into the plugin's JS engine:

1.  **Golden Manifest JSON**:
    *   On release, a compiler script compresses metadata (T-Numbers, definitions, Tiantai/Yogacara weights, and bidirectional links) of all 16,347 nodes into a highly optimized `dros_golden_manifest.json` (approx 5MB).
2.  **JS Graph Engine**:
    *   Loads this JSON directly in `main.ts` and implements the graph retrieval algorithm in TypeScript:
    ```typescript
    class DrosLocalEngine {
        private graph: Map<string, any> = new Map();

        async init(jsonData: any) {
            for (const key in jsonData) {
                this.graph.set(key, jsonData[key]);
            }
        }

        // O(1) millisecond local query
        lookup(term: string) {
            return this.graph.get(term) || null;
        }

        // Synaptic Weaving: identify all 16,347 terms in text and return coordinates
        weave(text: string): string[] {
            const matched: string[] = [];
            this.graph.forEach((value, key) => {
                if (text.includes(key)) matched.push(key);
            });
            return matched;
        }
    }
    ```
3.  **Direct LLM API Connection**:
    *   Users configure their personal `Gemini API Key` directly in Obsidian.
    *   The plugin performs graph retrieval and prompt assembly locally, fetching directly from the Google API via browser `fetch` without any server mediation. This guarantees **100% privacy and zero operational costs**.

---

## 🚀 5. Distribution Strategy

1.  **Testing Release (BRAT)**:
    *   Push repository to GitHub.
    *   Instruct beta testers to install the `BRAT` plugin and add the repository URL for quick updates.
2.  **Official Registry**:
    *   Submit a Pull Request to `obsidianmd/obsidian-releases`. Once approved, the plugin is searchable in the community store.
3.  **Data Monetization**:
    *   The plugin code is fully open-source under **AGPL-3.0**.
    *   The complete `dros_golden_manifest.json` dataset (16,347 verified concept nodes) is proprietary. The free version bundles 500 high-frequency terms, requiring a license key subscription to unlock the full database. This implements our dual-licensing strategy: **Open-Source Software, Commercial Data**.

---
*DROS v7.3 (Epistemic Edition) - Obsidian Plugin Development Blueprint. Created by Top Celestial Company Ltd. / Jimmy Chen.*

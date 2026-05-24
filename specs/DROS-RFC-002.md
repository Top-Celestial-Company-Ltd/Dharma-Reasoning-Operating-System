# DROS-RFC-002: Deterministic Keyword Routing via Trie (Weaver)
```text
Document Status: Standards Track
Authors: Jimmy Chen (Kang Chen Yuan Ltd.), Antigravity AI
Date: May 19, 2026
Version: 7.1.0
```

---

## Abstract

This document specifies the algorithmic standard for the **DROS Weaver**, the scanning layer responsible for intercepting user prompts and performing deterministic sliding-window tokenization. Unlike traditional statistical or neural tokenizers, the DROS Weaver utilizes a character-based Trie (Prefix Tree) and a **Longest Match First (LMF)** sliding window scanner. This guarantees $O(N)$ deterministic execution time and strict suppression of overlapping terms.

---

## 1. Algorithm Mechanics

To prevent semantic overlaps and fragmentation (e.g., matching the shorter word "般若" inside the longer canonical term "般若波羅蜜多"), the Weaver engine MUST execute the sliding LMF scan.

### 1.1 Trie Data Structure
Each node in the Trie structure MUST conform to the following abstraction:

```text
TrieNode {
    children: Map<Character, TrieNode>,
    nodeId: String | Null
}
```
- The `children` map MUST map single Unicode characters (UTF-16 code units or UTF-32 code points depending on language standards) to child nodes.
- The `nodeId` field contains the matching target node's T-Number if the path from the root to this node represents a valid canonical term or alias; otherwise, it MUST be `null`.

### 1.2 Sliding Window LMF Execution Flow

Given a source text string `T` of length `L`, and a Trie root `R`:

1. Initialize `i = 0`.
2. While `i < L`:
   a. Initialize `current = R`.
   b. Initialize `longestMatchNodeId = null`.
   c. Initialize `longestMatchLength = 0`.
   d. Set `j = i`.
   e. While `j < L`:
      - Retrieve character `c = T[j]`.
      - Find child node `next = current.children.get(c)`.
      - If `next` is null, break this inner loop.
      - Update `current = next`.
      - If `current.nodeId` is not null:
         * Update `longestMatchNodeId = current.nodeId`.
         * Update `longestMatchLength = j - i + 1`.
      - Increment `j`.
   f. If `longestMatchNodeId` is not null:
      - Emit a `DrosMatch` entity containing `(nodeId, startIndex = i, endIndex = i + longestMatchLength, matchedText = T[i ... i + longestMatchLength])`.
      - Advance the sliding index: `i = i + longestMatchLength` (suppressing sub-token matching).
   g. Else:
      - Increment `i = i + 1`.

---

## 2. Computational and Memory Complexity

### 2.1 Time Complexity
- **Boot Time (Trie Insertion)**: $O(M \times K)$, where $M$ is the number of terms (canonical + aliases) in the Manifest, and $K$ is the average character length of terms.
- **Scanning Time (Tokenization)**: $O(N)$, where $N$ is the character length of the input text. The maximum depth of any inner search path is bounded by the length of the longest registered term in the dictionary, ensuring constant-bound scaling.

### 2.2 Memory Complexity
- Trie memory footprint scales linearly with the number of unique character transitions. High-performance concurrent maps (e.g., Java's `ConcurrentHashMap` or C++'s `std::unordered_map`) SHOULD be used inside nodes to optimize concurrency without locking issues.

---

## 3. Multi-Language Parity Rules

To maintain cross-language parity, all micro-kernel implementations (C++, Go, Rust, Java, TypeScript, Python) MUST yield identical `DrosMatch` array outputs (matching starting index, ending index, and T-Numbers) for any given input UTF-8 string. Specially:
- All spaces and leading/trailing tabs of terms MUST be trimmed prior to insertion into the Trie.
- Matches MUST be case-insensitive for Western/Sanskrit-transliterated alphabet characters.

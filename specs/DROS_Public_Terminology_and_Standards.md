# DROS Public Terminology & Architectural Standards

**Document Status**: Official Public Standard  
**Authors**: Jimmy Chen (Top-Celestial Company Ltd.), Core Architecture Team  
**Version**: 1.0.0  

---

## 🏛 1. Purpose of this Document

In the absence of traditional software patents, the **Dharma Reasoning Operating System (DROS)** relies heavily on strict architectural standards, defined terminology, and open-source licensing (AGPL-3.0) to maintain its intellectual property boundaries.

This document serves as the **Official Lexicon and Standard** for the DROS ecosystem. Any third-party system, commercial platform, or academic research paper that utilizes these specific architectural concepts, data pipelines, or terminologies in the context of Large Language Model (LLM) reasoning engines is recognized as a derivative work of DROS and MUST comply with the underlying Open Source and Commercial licenses.

---

## 📖 2. Official Terminology (The Lexicon)

To establish a unified standard across all 6 micro-kernels (Rust, C++, Go, Java, TypeScript, Python) and the flagship `Dharma-Reasoning-Operating-System`, the following terms are strictly defined:

### 2.1 Core Entities

*   **Dharma Node (法義節點)**: 
    The fundamental unit of truth in DROS. Unlike vector chunks in traditional RAG, a Dharma Node is a deterministic, highly curated data structure (e.g., matching the `T-Number` format) representing a single canonical concept, complete with its historical aliases, definitions, and sect-specific resonance weights.
*   **Synapse (有向神經突觸)**: 
    The directed graph edge that connects two Dharma Nodes. It defines the strict semantic relationship (e.g., "equivalent to", "causes", "depends on") and carries a traversal weight, forming the deterministic reasoning path.
*   **Golden Manifest (黃金真理清單)**: 
    The cryptographically hashed `dros_golden_manifest.json` file. It is the absolute source of truth that the micro-kernels load into memory. Any tampering with this file violates the architectural standard.

### 2.2 System Components (The Pipeline)

*   **Weaver (編織者 / 攔截層)**: 
    The $O(N)$ deterministic Trie-based scanner that intercepts user prompts or LLM outputs. Its job is to perform Longest-Match-First (LMF) tokenization to identify all canonical terminology without statistical hallucination.
*   **Navigator (導航者 / 檢索層)**: 
    The graph-traversal engine. Once the Weaver identifies the entry nodes, the Navigator traverses the Synapses to pull the exact context, definitions, and logical boundaries required to answer the query.
*   **Guard VM (守門人虛擬機)**: 
    The final validation sandbox. It evaluates the LLM's generated response against the absolute truth defined in the Dharma Nodes to ensure zero semantic drifting (Hallucination = 0%).

---

## ⚙️ 3. Advanced Commercial Terminology (VajraClaw Enterprise)

While the foundational `1+6` ecosystem is open-sourced under AGPL-3.0, the core DROS maintainers reserve specific terminologies for proprietary, enterprise-grade, or highly specialized commercial products.

*   **VajraClaw (金剛爪)**: 
    The proprietary, commercial-grade orchestration layer for DROS. VajraClaw encompasses multi-tenant isolation, enterprise API rate limiting, distributed node clustering, and the proprietary deep-graph analytics algorithms not found in the public standard.
*   **Graphify (圖譜化)**: 
    The automated, AI-driven process of converting raw canonical texts (such as the DajueZang) into structured Dharma Nodes and Synapses. The algorithms used in Graphify are strictly proprietary and form the "Secret Sauce" of the DROS ecosystem.

---

## ⚖️ 4. Architectural Compliance & Licensing

If your system implements the Weaver-Navigator-Guard pipeline to deterministically control LLM hallucinations based on a structured graph of "Truth Nodes", you are operating within the DROS Architectural framework.

1.  **Open Source Compliance**: Any such system exposed over a network MUST fully open-source its entire stack under the **AGPL-3.0 License**.
2.  **Commercial Exemption**: To operate a closed-source or commercial derivative of the DROS Architecture, you MUST obtain a **VajraClaw Enterprise License** from the original authors.
3.  **Attribution**: You MUST retain the DROS-RFC nomenclature in your internal and external technical documentation.

*Powered by DROS - The Absolute Standard for Deterministic AI Reasoning.*

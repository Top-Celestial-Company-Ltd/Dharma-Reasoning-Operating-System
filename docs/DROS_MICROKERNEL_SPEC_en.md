# 📿 DROS Micro-kernel Standard Specification
## DROS-RFC 001: Unified Multi-Language µDROS Core Architecture

[繁體中文](DROS_MICROKERNEL_SPEC.md) | [English](DROS_MICROKERNEL_SPEC_en.md)

> **"One Specification to rule them all, One Manifest to bind them, One Topology to bring them all, and in the Offline Reasoning shine them."**  
> ── DROS Core Architects (Jimmy Chen & Antigravity)

---

## 🏛️ 1. Architectural Philosophy

The DROS Microkernel (µDROS Core) is designed with the core principles of **extreme lightweight footprint (<1000 lines), zero external dependencies, read-only in-memory topologies, and deterministic GuardVM contract enforcement**.

The Microkernel is **NOT** responsible for:
- Data persistence and writes (the Manifest is built at compile time; the microkernel loads it as read-only).
- High-dimensional vector similarity calculations (delegated to traditional RAG; DROS focuses on high-precision coordinate anchoring).
- LLM reasoning generation (DROS only constructs the hardened context prompt).

---

## 💾 2. DROS Golden Manifest Schema

All language implementations of the microkernel must parse and load the same `dros_manifest.json` structure:

```json
{
  "version": "7.3",
  "metadata": {
    "node_count": 16347,
    "compiled_at": "2026-06-08T12:00:00Z"
  },
  "nodes": {
    "T0001": {
      "id": "T0001",
      "canonical": "真如",
      "aliases": ["如如", "法性", "Suchness", "Tathata"],
      "weights": {
        "tiantai": 0.95,
        "yogacara": 0.90,
        "madhyamaka": 0.85
      },
      "definition": "The true nature of all phenomena, non-illusory, unchanging, the ultimate reality beyond words and conceptualization.",
      "synapses": [
        {"target": "T0002", "relation": "equivalent", "weight": 1.0},
        {"target": "T0005", "relation": "depend", "weight": 0.8}
      ]
    }
  }
}
```

### In-Memory Indexing Requirements
After loading the Manifest, the microkernel must compile two indexes in memory:
1. **NodeMap** (`ID -> Node`): For $O(1)$ node lookups via `T-Number`.
2. **AliasLookup** (`Alias -> ID`): Maps all canonical names and aliases (including English synonyms) to their corresponding `T-Numbers` for $O(1)$ anchoring during text scanning.

---

## ⚡ 3. Core Algorithm: Synaptic Weaver Engine

The Synaptic Weaver scans unstructured raw input text to extract all matching DROS concept nodes.

### 1. Inputs and Outputs
- **Input**: `text: String` (User query or the text of the note being edited)
- **Output**: `List[SynapseContext]` (A list of structures containing matched nodes, position indices, and topological weights)

### 2. Core Matching Rules
- **Longest Match First Principle**:
  If the text contains "大般若波羅蜜多經", and "大般若經", "般若", and "大般若波羅蜜多經" are all in the lookup dictionary, the engine must **preferentially and exclusively match the longest term** "大般若波羅蜜多經" to prevent synonym synapses from splitting.
- **Sliding Window Scanning or Trie Structure (Recommended)**:
  In Rust, C++, and TS, a Trie (Prefix Tree) is recommended to scan `AliasLookup` with $O(N)$ linear time complexity.

### 3. Scanning Algorithm Pseudocode
```text
function WEAVE(text: String, alias_lookup: Map<String, String>, node_map: Map<String, Node>) -> List<Match>:
    matches = []
    text_length = length(text)
    i = 0
    
    while i < text_length:
        longest_match_len = 0
        matched_node_id = null
        
        # Search for the longest matching alias starting from current position i
        for alias in alias_lookup.keys():
            alias_len = length(alias)
            if i + alias_len <= text_length:
                substring = slice(text, i, i + alias_len)
                if substring == alias:
                    if alias_len > longest_match_len:
                        longest_match_len = alias_len
                        matched_node_id = alias_lookup[alias]
                        
        if matched_node_id != null:
            matches.append(Match(
                node_id=matched_node_id,
                start_index=i,
                end_index=i + longest_match_len,
                matched_text=slice(text, i, i + longest_match_len)
            ))
            i += longest_match_len  # Step forward by longest match length to prevent overlaps
        else:
            i += 1  # No match, advance 1 character
            
    return matches
```

---

## 🕸️ 4. Topology Routing & Decay

When the scanner locates $K$ direct concept matches, the router expands outwards, grabbing the "first-order neighbors" connected to these core concepts and calculating decayed weights to prevent context window explosion.

### 1. Decay Formula
For a first-order neighbor $N_n$ of core node $N_c$:
$$W(N_n) = W_{edge}(N_c \rightarrow N_n) \times DecayFactor$$
*(Default $DecayFactor = 0.5$)*

### 2. Deduplication and Union
If a neighbor node is pointed to by multiple core nodes, its final topological weight is the sum (or maximum) of all incoming weights, representing the "resonance" of the neighbor node in the current conceptual web.

---

## 🛡️ 5. GuardVM Specification

GuardVM is a deterministic context prompt state machine. It filters and formats the output prompt according to loaded contract rules.

### 1. Vajra Contract Mode (Canonical Only)
- **Spirit**: Extremely rigorous. AI speculation is prohibited, forcing word-for-word alignment with canonical definitions.
- **GuardVM Behavior**:
  - Outputs only the `definition` of matched nodes.
  - Injects instructions into the Prompt: `"You MUST only answer based on the given definitions of the nodes below. If the query exceeds the definition scope, answer: '非本合約所及' (Beyond the scope of this contract)."`

### 2. Prajna Contract Mode (Speculative & Interpretive)
- **Spirit**: Inclusive. Guides the AI to perform cross-sectarian deductions, modern applications, and metaphorical transformations.
- **GuardVM Behavior**:
  - Outputs the semantic network of the core nodes and their first-order neighbors.
  - Injects instructions into the Prompt: `"Please perform sectarian synthesis and modern deduction along the topological synapse relations (e.g. 'rely', 'arise') based on the provided nodes."`

---

## 🚀 6. Output Weaving Template

All microkernels must compile the final context into a unified Markdown layout, appended to the System Prompt:

```markdown
<!-- DROS_SOVEREIGN_CONTEXT_START -->
## 📿 DROS Doctrinal Synaptic Grid (Sovereign Context Grid)
The following doctrinal synapses have been successfully woven into the current text:

### Canonical Core Nodes
- **T0001 (真如)**: The true nature of all phenomena...

### Active Synaptic Neighbors
- **T0002 (法性)** (Resonance Weight: 0.50): Woven with [真如] via [equivalent] relationship.

### GuardVM Execution Mode: Vajra
[Vajra Contract Active]: All your reasoning MUST be 100% restricted to the canonical definitions above. Do not introduce unauthorized religious speculations!
<!-- DROS_SOVEREIGN_CONTEXT_END -->
```

---
*DROS Specification v7.3 (Epistemic Edition). Authored by Antigravity.*

# DROS-RFC-003: GuardVM & Inference Contracts
```text
Document Status: Standards Track
Authors: Jimmy Chen (Kang Chen Yuan Ltd.), Antigravity AI
Date: May 19, 2026
Version: 7.1.0
```

---

## Abstract

This document formalizes the execution specifications for the **DROS GuardVM (Virtual Machine)** and the inference contract compiler profiles. The GuardVM is a runtime sandboxing and policy-enforcement layer that structures, restricts, and virtualizes the context injected into the Large Language Model (LLM). This specification standardizes the mathematical formula for topological decay, resonance summation, and the structured XML-style delimiters for sandbox injection.

---

## 1. Topological Navigation & Decay Mathematics

When canonical core nodes are matched by the DROS Weaver, the **DROS Navigator** walks the graph database to evaluate related concepts.

### 1.1 Synaptic Weight Decay Formula
For each matched core node $C \in \mathbf{Matches}$, it contains synapses pointing to adjacent nodes $A$. The decayed weight $W_d(A)$ transmitted through a synapse is defined as:

$$W_d(A) = W_s(C \to A) \times \gamma$$

Where:
- $W_s(C \to A)$ is the original static synapse weight registered in the golden database manifest.
- $\gamma \in [0.0, 1.0]$ is the runtime decay factor (default: $0.5$).

### 1.2 Resonance Summation (Co-occurrence Integration)
If an adjacent node $A$ is pointed to by multiple matched core nodes (co-occurrence), its active topological resonance weight $W_{\text{resonance}}(A)$ converges through summation:

$$W_{\text{resonance}}(A) = \sum_{C \in \mathbf{Matches}} (W_s(C \to A) \times \gamma)$$

To prevent redundant indexing, adjacent nodes that are already matched as core nodes MUST be pruned:

$$\text{If } A \in \mathbf{Matches} \implies A \text{ is excluded from active neighbors.}$$

---

## 2. GuardVM Execution Profiles (Contracts)

The GuardVM compiler MUST compile the final context prompt using one of the following two contract profiles:

### 2.1 Vajra Profile (Strict Constraint Mode)
- **Design Intent**: Designed for mission-critical, high-risk doctrinal reasoning where logic derivation MUST be strictly factual and literal.
- **Rules**:
  - The compiled prompt MUST contain only the definitions of the matched core nodes.
  - Active synaptic neighbors MUST be 100% stripped and excluded from prompt compilation.
  - The engine MUST append a strict boundary constraint instruction forcing the LLM to output "非本合約所及" (Beyond active contract) if the query exceeds the provided definitions.

### 2.2 Bodhisattva Profile (Adaptive Semantic Expansion Mode)
- **Design Intent**: Designed for scholastic, comparative, or educational interpretations where adaptive semantic routing is encouraged.
- **Rules**:
  - The compiled prompt MUST include both core node definitions and active synaptic neighbors sorted in descending order of $W_{\text{resonance}}(A)$.
  - The compiler MUST append an adaptive guidance instruction allowing the LLM to bridge doctrines utilizing the active neighbor relationships (e.g., identity, dependence).

---

## 3. Sandbox Prompt Serialization Standard

All DROS implementation engines MUST compile the prompt wrapping the context in standard XML-style comments for parser security:

```markdown
<!-- DROS_SOVEREIGN_CONTEXT_START -->
## 📿 DROS 拓撲義理網格 (Sovereign Context Grid)
當前文本中已成功編織以下義理突觸：

### 核心名相定義 (Canonical Core Nodes)
- **[Canonical Name] ([T-Number])**：[Definition]

### 關聯拓撲鄰居 (Active Synaptic Neighbors) [Prajna Mode Only]
- **[Neighbor Name] ([T-Number])** (共鳴權重: [W_resonance])：與 [[Source Name]] 具有 [[Relation]] 關係。

### 推理合約熔斷規則 (GuardVM Execution Mode: [VAJRA | PRAJNA])
[Strict or Expansionary Doctrinal Instructions]
<!-- DROS_SOVEREIGN_CONTEXT_END -->
```
This precise serialization standard ensures that LLM parses the sandboxed boundaries cleanly, preventing prompt injection attacks from overlapping user content.

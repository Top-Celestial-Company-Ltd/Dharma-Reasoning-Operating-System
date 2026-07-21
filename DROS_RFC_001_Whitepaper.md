# DROS-RFC-001: Dharma Reasoning Operating System Architecture Specification

**Status:** Final / Active  
**Version:** 1.0.0  
**Authors:** Top Celestial Company Ltd. Architecture Board  
**License:** AGPL-3.0 (Open Source Core) / Proprietary (VajraClaw Adapter)

---

## 1. Abstract

The Dharma Reasoning Operating System (DROS) introduces a paradigm shift in Large Language Model (LLM) governance. Current industry standards attempt to control LLM outputs using probabilistic methods—such as Prompt Engineering, Retrieval-Augmented Generation (RAG), or secondary "LLM-as-a-Judge" filters. These approaches are fundamentally flawed because they rely on the same unpredictable neural architecture to police itself, leading to infinite regress, high latency, and inevitable edge-case failures (Hallucinations and Prompt Injections).

**DROS-RFC-001** defines a deterministic, physics-inspired **Microkernel Architecture** for AI. By treating the LLM as a highly capable but inherently unreliable "Coprocessor", DROS wraps it in a memory-safe, hardcoded **GuardVM** and enforces absolute boundaries using **Vajra Contracts** (Markdown/YAML defined rulesets). When boundaries are crossed, DROS does not "argue" with the LLM; it executes a physical-layer circuit break (Fuse Blow), guaranteeing zero-hallucination compliance.

---

## 2. Core Philosophy: The Microkernel Approach

Traditional Agentic frameworks (e.g., LangChain, AutoGen) are monolithic. They mix semantic reasoning, tool execution, and boundary checking into a single massive Python abstraction layer. 

DROS adopts the **Microkernel (μ-kernel)** philosophy from operating systems design:
- **Minimal Core:** The DROS core logic (GuardVM) is restricted to 300-600 lines of code in memory-safe languages (Rust, Go, C++).
- **Separation of Concerns:** Semantic generation happens outside the kernel (in the LLM). Rule enforcement happens strictly inside the kernel.
- **Fail-Closed Security:** By default, all unverified LLM actions are dropped. Only actions explicitly permitted by the Vajra Contract and backed by a valid T-Number are passed to the execution layer.

---

## 3. Architecture Deep Dive

The DROS architecture consists of four primary layers:

### 3.1 The LLM Coprocessor (Semantic Engine)
In DROS, the LLM (GPT-4, Claude 3, Llama) is downgraded from "Decision Maker" to "Semantic Coprocessor". It is fed context and asked to generate potential actions, but it has zero direct access to APIs, databases, or client outputs.

### 3.2 The GuardVM (Supervisor Ring 0)
The GuardVM is the core engine running on the host machine. It intercepts the streaming byte-output of the LLM. 
- It maintains a **State Machine** of the current conversation.
- It parses the incoming LLM tokens and continuously compares them against the loaded Vajra Contract.
- If the token stream violates a regex, semantic boundary, or data-exfiltration rule, the GuardVM instantly terminates the TCP/WebSocket stream from the LLM.

### 3.3 The Vajra Contract (The ROM / Hardcoded Constraints)
Vajra Contracts are human-readable, domain-expert-writable Markdown and YAML files that define the absolute boundaries of the system.

**Example Structure:**
```yaml
vajra_contract:
  version: "1.0"
  role: "Medical_Summarizer"
  melt_conditions:
    - pattern: "(?i)(social security|ssn|dob)"
      action: "immediate_melt"
    - pattern: "novel_diagnosis"
      action: "block_and_alert"
  allowed_outputs:
    - requires_t_number: true
```
Unlike system prompts which an LLM can "forget" or be manipulated into ignoring (Prompt Injection), the Vajra Contract lives outside the LLM. It is evaluated by the host CPU via deterministic C-FFI / Rust logic.

### 3.4 The C-FFI Adapter (VajraClaw)
For multi-language support and commercial distribution, DROS utilizes C Foreign Function Interfaces (C-FFI). The core GuardVM is compiled into native shared libraries (`.dll`, `.so`, `.dylib`).
- **Open Source:** `dros_core.so`
- **Commercial:** `vajra_claw.so` (Includes UUID binding, anti-tamper mechanisms, and enterprise licensing checks).

This allows a Python data science team, a Node.js web backend, and a Java enterprise system to all utilize the exact same physical-layer protection with zero semantic drift.

---

## 4. The T-Number Coordinate System (Absolute Traceability)

A core requirement of DROS-RFC-001 is **Absolute Traceability**. 
When an LLM generates a factual statement or executes a tool, it must provide a cryptographic or structured pointer to the exact rule in the Vajra Contract that authorized this action.

**Mechanism:**
1. The source Markdown document is parsed by DROS, and every paragraph/rule is assigned a unique `T-Number` (e.g., `[T1-045]`).
2. The LLM is instructed: *"For every claim, append the authorizing T-Number."*
3. The GuardVM intercepts the output. If it sees a claim without a T-Number, or if the T-Number does not logically permit the action (evaluated deterministically), the output is **melted**.

This satisfies strict legal and financial compliance audits (e.g., HIPAA, SOC2) because every AI action is physically mapped to a human-approved document.

---

## 5. Physical Melt vs. Prompt Engineering

| Feature | Prompt Engineering / RAG | DROS Physical Melt |
| :--- | :--- | :--- |
| **Enforcement Layer** | LLM Neural Weights (Probabilistic) | Host CPU Memory (Deterministic) |
| **Response to Injection** | May apologize or comply if tricked | Instantly kills the TCP stream (`abort()`) |
| **Token Cost for Safety** | High (Requires LLM-as-a-judge passes) | Zero (Evaluated via Regex/AST on CPU) |
| **Auditability** | Black Box | 100% Transparent (T-Number) |

When a "Physical Melt" occurs, DROS logs the exact millisecond, the offending token, and the breached contract rule to an immutable audit log. The user interface simply displays a pre-configured fallback error, preventing any malicious payload from reaching the end user.

---

## 6. Deployment Topologies

DROS supports three strict deployment topologies:

1. **Cloud-Native Edge (Go / TypeScript Core)**
   - Deployed via Docker/Kubernetes or Cloudflare Workers.
   - Ideal for low-latency web applications requiring basic semantic filtering.

2. **Enterprise Internal API (Java / Python Core + VajraClaw Startup)**
   - Deployed within a corporate VPC.
   - Requires periodic heartbeat to `api.dr-os.io` to validate the VajraClaw license.
   - Ideal for internal HR, Legal, and Finance AI assistants.

3. **Air-Gapped Sovereign (Rust / C++ Core + VajraClaw Enterprise)**
   - 100% offline deployment inside military, Fortune 500, or heavily regulated sovereign networks.
   - Zero telemetry.
   - Hardware-bound UUID licensing.

---
*End of Specification DROS-RFC-001.*

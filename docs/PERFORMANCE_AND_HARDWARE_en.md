# ⚙️ DROS Performance & Hardware Guide

[繁體中文](PERFORMANCE_AND_HARDWARE.md) | [English](PERFORMANCE_AND_HARDWARE_en.md)

Welcome to the DROS (Dharma Reasoning OS) Performance & Hardware Configuration Guide! This document resolves any doubts regarding "running speed" and "computer specifications," providing optimization tips for the best experience.

---

## 🎯 Core Verdict

> [!NOTE]
> **"Extremely Green, Zero Hardware Barriers!"**
> DROS adopts a **"Cloud Heavy Reasoning + Local Lightweight Grid"** architecture. Whether you are using a high-end gaming workstation or a decade-old entry-level laptop, the running and response speed of DROS **remains virtually identical, with no physical difference**!

---

## 🧠 Local Resource Footprint

DROS is designed from the ground up to minimize local hardware requirements. Below is the resource profile during active execution:

| Resource | Measured Usage | Technical Detail | Hardware Requirement |
| :--- | :--- | :--- | :--- |
| **🎮 Graphics Card (GPU)** | **0% (Completely Unused)** | Complex LLM reasoning is outsourced to Google Cloud. No local GPU is needed. | **No GPU Requirement** (Integrated graphics are sufficient) |
| **🧠 Memory (RAM)**| **< 40 MB** | The `gemini_proxy.py` script and the local Trie compiler are lightweight. | **Negligible Footprint** (Runs easily on 2GB RAM legacy devices) |
| **⚡ Processor (CPU)** | **< 1%** | The local system only executes $O(1)$ string matching and HTTP routing. | **Any Dual-Core Processor** |
| **💾 Disk Space** | **< 10 MB** (Excl. scriptures) | Core scripts are compact. Terminology nodes and texts are plain Markdown text. | **Any Disk Storage** |

---

## ⚡ Three Laws of Response Latency (Time to First Token)

Since DROS performance is independent of local PC hardware, what factors determine response latency? It is guided by these three external dimensions:

### 1. 🌐 Network Latency —— **70% Influence**
* **Principle**: The local DROS proxy establishes direct HTTPS connections to Google AI Studio API servers.
* **Impact**: The **Ping latency** between your local PC and Google servers is the primary bottleneck. A smooth, stable network route (or proxy endpoint) dramatically improves token emission speed.

### 2. Cloud LLM Generation Time —— **25% Influence**
* **Gemini 2.5 Flash-Lite (Fast Search / Router)**: High response speed. Time to first token is usually between **0.5 to 1 second**.
* **Gemini 3.1 Pro (Deep Scholastic Study)**: Employs deep reasoning. Response latency is slightly higher at **1 to 2 seconds**, but produces superior analytical depth.

### 3. NotebookLM Semantic Search Fallback —— **5% Influence**
* **Trigger**: When a keyword in your query does not match a hardened node in the local Wiki, the system performs a fallback semantic query via the Google NotebookLM CLI.
* **Impact**: The cloud vector RAG query introduces an additional round-trip latency of **1 to 2 seconds** before streaming output begins.

---

## 🚀 Optimization Tips

To make your DROS dialogs stream like a typewriter, follow these optimization guidelines:

### 1. ⚡ Optimize Network Routes
* Select network endpoints with the **lowest Ping latency and highest stability** (typically USA nodes or nodes close to Google backbone networks). This shortens first-token latency to under 1 second.

### 2. 🗿 Enrich Local Terminology Wiki
* Keep your local `core/` or `User_Pavilion/` folders rich. When your query hits a matching Markdown term file in the local Wiki, the Trie compiler intercepts it with **zero latency**, bypassing the 2-second cloud RAG search delay.

### 3. ⚖️ Select the Appropriate Contract Mode
* **Vajra Mode (Strict)**: Forces compact, highly cited scripture outputs. Fewer generated words mean **faster overall output and lowest token consumption**.
* **Bodhisattva Mode**: Allows associative thinking and modern interpretations. Outputs are longer and ideal for quiet, deep study.

---
*Dharma Reasoning OS v7.3 — Lightweight Wisdom, Fluent Dharma Sounds.*

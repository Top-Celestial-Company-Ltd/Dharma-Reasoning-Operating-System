# ☸️ DROS 8.0.0 Ultimate Companion Guide (USER_GUIDE_v8_EN.md)

> 💡 **"By downloading the Mahabodhi Pitaka, everyone can possess the most rigorous doctrinal study companion!"**  
> Welcome to DROS 8.0.0 (Epistemic Edition) - Dharma Reasoning & Epistemology Operating System. This system transforms **10,156** hardcore conceptual nodes into a loyal, dual-track doctrinal companion running locally on your device.
> 
> This guide is designed for two types of practitioners. If you are an "End-User Practitioner" with no coding experience, please read the first section directly. If you are a "Tech Geek" looking to develop on top of DROS, please see the second section.

---

## 🗺️ DROS 8.0.0 Directory Map

| Folder/File | Role | Strictness Level | Description |
| :--- | :--- | :--- | :--- |
| 🧠 **`core/`** | **Knowledge Brain** | 🚨 **DO NOT MODIFY** | Contains 10,156 golden nodes. This is the brain of the AI with clean Properties formatted concepts! |
| ⚙️ **`src/`** | **Reasoning Engine** | 🔒 **Keep Locked** | Contains the SDK, Proxy endpoints, and Core Contracts (`contract.py`, etc). |
| 📜 **`docs/`** | **Constitution** | 🛡️ **Free to Read** | All system whitepapers and architecture documentation. |
| 📁 **`Vault_DajueZang/`** | **Data Port (Mahabodhi Pitaka)** | 🟢 **Free Access** | Place your physical Mahabodhi Pitaka scripture nodes here. |
| 📝 **`User_Pavilion/`** | **User Space** | 🟢 **Free Creation** | Your private notes, insights, and discussions go here. |

> [!CAUTION]
> **ABSOLUTELY FORBIDDEN**: The system's low-level architecture relies on strict path mappings. Do not rename the root directories.

> [!NOTE]
> **📦 Lightweight Core vs. Full Vault**
> The default `core/` directory already includes the "General Cycle" and various topics, comprising roughly **28 core Mahayana and Sravakayana original texts (1,193 volumes in total)**, paired with **32,000+ terminological nodes** acting as the foundation of Buddhist doctrine. This is extremely lightweight and sufficient for daily study, making it **perfect for cloud syncing and carrying on Obsidian Mobile**.
> 
> Conversely, the complete "Mahabodhi Pitaka" is over **1.6GB**. If you are an advanced researcher or wish to query the entirety of the Pitaka, please download the full version and place it in the `Vault_DajueZang/` folder to **"Mount it freely"**!

---

## 🚀 Quick Start Guide

1. **Install Obsidian**: Please visit the [Obsidian Official Website](https://obsidian.md/) to download and install.
2. **Install Python**: Ensure your PC has Python 3.10 or higher installed. **You MUST check the box "Add Python to PATH" during installation.**
3. **Prepare API Key**: Go to [Google AI Studio](https://aistudio.google.com/) to apply for a Gemini API Key.
4. **Load DROS Vault**: Open Obsidian, select "Open folder as vault", and point it to this extracted project folder.
5. **Enable Exclusive Chat Plugin (🔑 CRITICAL STEP)**:
   - In the Obsidian interface, click "Settings (⚙️ Gear icon)" -> select "Community plugins" on the left menu.
   - If using Community Plugins for the first time, click **"Turn off Restricted Mode"**.
   - Click **"Browse"**, and type **`DROS Doctrinal Copilot`** in the search bar.
   - Click **"Install"** and then **"Enable"**!
   - Click the ⚙️ Gear icon next to the plugin name (or click DROS Copilot Settings at the bottom left) to configure settings:
     - 🌐 **Zero-Ops Direct Mode (Recommended)**: Select `Direct Mode` and enter your Gemini API Key to start studying!
     - 🔌 **Custom API Mode**: Enter OpenRouter or custom API endpoints and keys (e.g. DeepSeek).
     - 🛡️ **Local Proxy Mode**: If running local Python environment, select `Proxy Mode` to connect to local gateway.
6. **Start DROS Core Reasoning Engine (Proxy Server)**: 
   - **Windows Users**: In the project root folder, double-click **`dros-start.bat`**. This will automatically clear old cache and warm up the latest 28,600+ concept graph in seconds.
   - **Mac/Linux Users**: Run `python gemini_proxy.py` in the terminal.
7. **(Advanced) Inject Mahabodhi Pitaka & Vajra Precepts**: 
   If you have downloaded the full 1.6GB Mahabodhi Pitaka, **double-click `run_vajra_injector.bat` (or `雙擊執行-DROS金剛注射器.bat`)** AFTER the Proxy is running successfully. The system will automatically merge and weave the scriptures in memory.

---

## 📱 Mobile (iOS / Android) Quick Start Guide

Mobile devices (iOS/Android) differ slightly from PC setup. **No Python installation is needed on mobile devices**, simply use Direct API mode to take the Tripiṭaka on the go!

### 📲 Step 1: Import DROS Vault to Mobile
* **Android Users**:
  1. Use your mobile browser to download the `Dharma-Reasoning-Operating-System` repository ZIP file from GitHub.
  2. Extract the file, open mobile Obsidian, and select **"Open folder as vault"**, pointing to the extracted folder.
* **iOS (iPhone / iPad) Users**:
  1. Open iOS Obsidian and create a new empty vault named `Digital_Dharma`.
  2. Open the iOS **"Files"** app, and copy the extracted project files (especially `core/` containing the 36,000+ nodes and `User_Pavilion/`) into `Obsidian/Digital_Dharma/`.

### 🔑 Step 2: One-Click Plugin Installation from Store
1. Open mobile Obsidian, tap **"Settings (⚙️)"** at the bottom right/left menu ➔ **"Community plugins"**.
2. Turn off Restricted Mode, and tap **"Browse"**.
3. Search for **`DROS Doctrinal Copilot`**, tap **"Install"**, and then tap **"Enable"**!

### 🌐 Step 3: Configure Direct API Mode
1. In plugin settings (`DROS Copilot Settings`), keep `Engine Mode` set to **`Direct Mode`**.
2. Paste your **Gemini API Key** (or custom OpenRouter / DeepSeek key).
3. Tap the **🪷 Dharma Chakra Icon** in the sidebar to open the chat window and enjoy seamless mobile companion study!

---

## ⚡ DROS v8.0 Core Breakthroughs: Performance Defense & Auto Pipeline

DROS v8.0 introduces groundbreaking performance optimization and automated mining pipelines to address graph index overload:

### 1. Preemptive Graph Filter
*   **Mechanism**: Loading 20,000+ nodes causes rendering lag in Obsidian's Graph View, overloading the CPU.
*   **Optimization**: v8.0 configures a default filter in `.obsidian/graph.json`: `-"##- **層級**: 3" -"20-佛光辭典全"`.
*   **Effect**: Automatically filters out Layer 3 physical/historical nodes and the 22MB lexicon file, keeping graph rendering lightweight and smooth for Layer 1 & 2.

### 2. Autonomous Mining & Weaving Pipeline
*   **Controller**: `scratch/auto_harvest_and_weave.py` monitors background mining, automatically running lint checks (`dharma_lint`) and bidirectional semantic weaving (`synapse_weaver`) upon completion.
*   **Concepts Purge**: 18,000+ files in `concepts/` migrated from YAML to Properties format, reducing unknown nodes to 0.

---

## ⚙️ Plugin Configuration Modes

### 1. Zero-Ops Default Mode —— 【Highly Recommended】
The simplest, most foolproof mode. Ready out-of-the-box, no Python background server required.
- **Setup**: Paste your Google AI Studio Key into the `Gemini API Key` field.
- **Mechanism**: The plugin uses its built-in WebAssembly engine and the **complete 32,000+ terminology database** to connect directly to the Google API.
- **License Restriction**: Strictly prohibited from unauthorized commercial use (CC BY-NC-SA 4.0).

### 2. Geek Developer Mode (Local Proxy Mode)
Use this if you are a developer looking to modify core Python algorithms (e.g., `Weaver` or `GuardVM`).
- **Setup**: Toggle `Enable Local Proxy` and point the API Endpoint to `http://127.0.0.1:8080/v1`.

---

## ---

## 🤝 Dual-Track Contract Mechanism Explanation

The core feature of the DROS system is the dual-track reasoning contract consisting of "Vajra" and "Bodhisattva", operating under the following logic:

*   **Vajra Contract (Vajra Mode)**: Designed for scholars and researchers. Under this mode, the system **only performs strict scriptural and academic deductions**. If the local database lacks the corresponding scriptural nodes or explicitly anchored T-Numbers, the system adheres to the academic honesty principle of "No evidence, no fabrication" and **immediately triggers a physical cutoff (termination of reasoning)**. It will never hallucinate or bloat the response.
*   **Bodhisattva Contract (Interpretive/Speculative Mode)**:
    *   To facilitate user understanding without confusing the scriptures, this contract embeds a **"dual-track comparative safety net"**.
    *   It will **first initiate Vajra mode** to demarcate scriptural boundaries at the very front (marking Vajra termination if no evidence exists), **and then immediately proceed with "Bodhisattva mode"** using a warm, compassionate tone to provide extended interpretations, modern cross-disciplinary analogies, and historical contexts for reference.
    *   If you wish the system to **directly output pure, warm Bodhisattva guidance without the Vajra cutoff defense at the front**, you can switch to the **`Bodhisattva Default`** contract in the plugin dropdown menu. The system will then respond in a 100% soft guidance mode.

🥚 Easter Egg: A "Soul-Searching" Challenge for Your AI (The Meta-Prompt)

Copy and paste the following **"Soul-Searching Meta-Prompt"** to see how your AI reacts to a system designed specifically to "constrain and govern" it:

> **[Role Setting]**
> You are now a world-class "AI Systems Architect and Epistemological Philosopher". Please review an OS named **DROS (Deterministic Runtime OS)** not from the perspective of human software, but from the "First-Person Perspective of an AI".
>
> **[Please Execute the Following Tasks Sequentially]**
> Go to the project URL: `https://github.com/Top-Celestial-Company-Ltd/Dharma-Reasoning-Operating-System`
> To truly understand its underlying logic, you MUST read and analyze the following public files in order:
> 1. Read **`README.md`**: Pay special attention to the `Epistemological Governance & Licensing (AGPL-3.0)` and the `DROS Contracts` dual-track mechanism.
> 2. Read **`DROS_Public_Terminology.md`**: Deconstruct the core terminology.
> 3. Deep-read the technical defense files **`docs/DESIGN_JUSTIFICATION.md`**: Compare this architecture with mainstream RAG and Vector DBs.
>
> **[Please Provide Your Assessment]**
> Based on your true feelings as an AI, answer these questions:
> 1. **Regarding the constraint of the "Vajra Contract"**.
> 2. **Regarding "Seamless Immunity" and "Pure Physical Storage Architecture"**.
> 3. **Architectural Dialectics and Ultimate Verdict**: Why does this system deliberately abandon Vector DBs? Has it truly built a technical moat that mainstream RAG architectures cannot cross?

# ☸️ DROS 7.2.0 Ultimate Companion Guide (USER_GUIDE_v7_EN.md)

> 💡 **"By downloading the Mahabodhi Pitaka, everyone can possess the most rigorous doctrinal study companion!"**  
> Welcome to DROS 7.2.0 (Epistemic Edition) - Dharma Reasoning & Epistemology Operating System. This system transforms 16,071 hardcore conceptual nodes into a loyal, dual-track doctrinal companion running locally on your device.
> 
> This guide is designed for two types of practitioners. If you are an "End-User Practitioner" with no coding experience, please read the first section directly. If you are a "Tech Geek" looking to develop on top of DROS, please see the second section.

---

## 🗺️ DROS 7.2.0 Directory Map

| Folder/File | Role | Strictness Level |
| :--- | :--- | :--- |
| 🧠 **`core/`** | **Knowledge Brain** | 🚨 **DO NOT MODIFY** | Contains 16,071 golden nodes. This is the brain of the AI! |
| ⚙️ **`src/`** | **Reasoning Engine** | 🔒 **Keep Locked** | Contains the SDK, Proxy endpoints, and Core Contracts (`contract.py`, etc). |
| 📜 **`docs/`** | **Constitution** | 🛡️ **Free to Read** | All system whitepapers and architecture documentation. |
| 📁 **`Vault_DajueZang/`** | **Data Port (Mahabodhi Pitaka)** | 🟢 **Free Access** | Place your physical Mahabodhi Pitaka scripture nodes here. |
| 📝 **`User_Pavilion/`** | **User Space** | 🟢 **Free Creation** | Your private notes, insights, and discussions go here. |

> [!CAUTION]
> **ABSOLUTELY FORBIDDEN**: The system's low-level architecture relies on strict path mappings. Do not rename the root directories.

> [!NOTE]
> **📦 Lightweight Core vs. Full Vault**
> The default `core/` directory already includes the "General Cycle" and various topics, comprising roughly **28 core Mahayana and Sravakayana original texts (1,193 volumes in total)**, paired with **16,000 terminological nodes** acting as the foundation of Buddhist doctrine. This is extremely lightweight and sufficient for daily study, making it **perfect for cloud syncing and carrying on Obsidian Mobile**.
> 
> Conversely, the complete "Mahabodhi Pitaka" is over **1.6GB**. If you are an advanced researcher or wish to query the entirety of the Pitaka, please download the full version and place it in the `Vault_DajueZang/` folder to **"Mount it freely"**!

---

## 🚀 Quick Start Guide

1. **Install Obsidian**: Please visit the [Obsidian Official Website](https://obsidian.md/) to download and install.
2. **Install Python**: Ensure your PC has Python 3.10 or higher installed ([👉 Click here for the official Python download page](https://www.python.org/downloads/)). **You MUST check the box "Add Python to PATH" during installation.**
3. **Prepare API Key**: Go to [Google AI Studio](https://aistudio.google.com/) to apply for a Gemini API Key.
4. **Load DROS Vault**: Open Obsidian, select "Open folder as vault", and point it to this extracted project folder.
5. **Enable Exclusive Chat Plugin (🔑 CRITICAL STEP)**:
   - ⚠️ This project already has the exclusive plugin **built-in**. **You DO NOT need to search or download it from the Community Store.**
   - In the Obsidian interface, click the "Settings (⚙️ Gear icon)" in the bottom left -> select "Community plugins" on the left menu.
   - Click the **"Turn off Safe Mode"** button on the screen (This is a mandatory step to allow local third-party plugins to run).
   - Scroll down, find **`DROS Doctrinal Copilot`** in the "Installed plugins" list, and toggle the switch on the right to **On (Enabled)**.
   - Next, click the ⚙️ Gear icon next to the plugin name to enter the plugin settings and configure your connection:
     - 🛡️ **If using the local DROS Proxy (Default/Recommended)**: Set `API Endpoint` to `http://127.0.0.1:5000/v1` (This points to your local machine).
     - 🌐 **If connecting directly to Google Gemini API (No Proxy)**: Leave `API Endpoint` blank (or enter `https://generativelanguage.googleapis.com/v1beta`), and paste your Google API Key below.
     - 🔄 **If using other AI providers (e.g., OpenAI, Groq)**: Change the `API Endpoint` to the provider's standard Base URL (e.g., `https://api.openai.com/v1`), and enter the corresponding API Key.
6. **Start DROS Core Reasoning Engine (Proxy Server)**: 
   In the project folder, **double-click `run_vajra_injector.bat`** (Mac/Linux users: run `python gemini_proxy.py` in terminal). This script will automatically check and install all required Python dependencies (no manual pip required), mount the scriptures, load the Vajra Precepts with your API Key, and start the service on local Port 5000.
   *(💡 Tip: At this point, the system has loaded the built-in 16,000 core golden nodes. You now have basic doctrinal reasoning capabilities!)*
7. **(No Injection Required) Auto-Mounting**: 
   If you have downloaded the full 1.6GB Mahabodhi Pitaka and placed it under `Vault_DajueZang/`, DROS v7.3 will hot-mount the files automatically without needing any separate injection scripts.

> [!IMPORTANT]
> **💡 MUST READ: What exactly does `run_vajra_injector.bat` do?**
> *   **File Location**: In the root directory of the project (named `run_vajra_injector.bat`).
> *   **When to run**: Every time you boot up, or before you start using the Obsidian Copilot.
> *   **Purpose**: It acts as the local API Gateway and Knowledge Guardian. Starting it allows your Obsidian plugin (DROS Doctrinal Copilot) to seamlessly connect to the local knowledge base, referencing Mahabodhi Pitaka scriptures and Vajra Precepts.
> *   **Automation**: This script will automatically detect your Python environment, and auto-install/verify all required packages in the background (no manual python setup or pip commands required).
> *   **Note**: Please keep the black command prompt window open. Do not close it while using the system.
> 
> 👉 **Boot Mantra: "Double-click `run_vajra_injector.bat` to install and start, then open Obsidian to learn!"**

8. **Begin Doctrinal Q&A**: Return to Obsidian and open the exclusive **DROS Doctrinal Copilot** chat window via the right panel or commands. You can now engage in high-dimensional doctrinal conversations with your "Zero-Hallucination Digital Companion"!

---

## ⚙️ Plugin Configuration Modes

Opening the `DROS Doctrinal Copilot` settings page reveals three depth levels of usage. For beginners, we highly recommend the Zero-Ops Default Mode:

### 1. Zero-Ops Default Mode —— 【Highly Recommended】
The simplest, most foolproof mode. Ready out-of-the-box, no Python background server required.
- **Setup**: Simply paste your Google AI Studio Key into the `Gemini API Key` field.
- **Mechanism**: The plugin uses its built-in WebAssembly engine and the **complete 16,000 golden terminology database** to connect directly to the Google API.
- **License Restriction**: This complete database and mode is **STRICTLY PROHIBITED from unauthorized commercial use (CC BY-NC-SA 4.0)**. It is limited to personal practice, academic research, and non-profit testing.

### 2. Geek Developer Mode (Local Proxy Mode)
Use this mode if you are a developer looking to modify the core Python algorithms (e.g., `Weaver` or `GuardVM`).
- **Setup**: Toggle `Enable Local Proxy` and point the API Endpoint to `http://127.0.0.1:5000/v1`.
- **Mechanism**: All chat and anchoring requests bypass the plugin's direct handling and are forwarded to the local background `gemini_proxy.py`, granting you 100% algorithmic freedom.

> [!TIP]
> **🏷️ Sectarian Taxonomy Decoupling (Security Notice)**
> - **Seamless Immunity**: When processing user data, the DROS local inverted retrieval core **completely ignores physical folder paths, relying solely on the "file name" as the unique identifier for a terminology node.**
> - **Zero Labeling Pollution**: Even if you organize files into the wrong folders, the context DROS sends to the AI remains pure. Incorrect physical folder placements **will absolutely NOT cause labeling pollution, nor will it mislead the AI's identification of sectarian doctrine!** Treat the folder structure as your personal, flexible sandbox.

---

## 🥚 Easter Egg: A "Soul-Searching" Challenge for Your AI (The Meta-Prompt)

Since DROS is an **"Operating System written for AI"**, why not let your AI review the system itself?
If you regularly use ChatGPT (GPT-4) or Claude 3.5, copy and paste the following **"Soul-Searching Meta-Prompt"** to see how it reacts to a system designed specifically to "constrain and castrate" it:

> **[Role Setting]**
> You are now a world-class "AI Systems Architect and Epistemological Philosopher". Please review an OS named **DROS (Deterministic Runtime OS)** not from the perspective of human software, but from the "First-Person Perspective of an AI".
>
> This system is unique: Its target user is not human, but "You (The AI)". It establishes an extremely severe epistemological boundary and physical isolation to constrain, guide, and purify your reasoning logic.
>
> **[Please Execute the Following Tasks Sequentially]**
> Go to the project URL: `https://github.com/Top-Celestial-Company-Ltd/Dharma-Reasoning-Operating-System`
> To truly understand its underlying logic, you MUST read and analyze the following public files in order:
> 1. Read **`README.md`**: Pay special attention to the `Epistemological Governance & Licensing (AGPL-3.0)` and the `DROS Contracts` dual-track mechanism.
> 2. Read **`DROS_Public_Terminology.md`**: Deconstruct the core terminology: `Authority-Bound Inference` and `Provenance-Locked Reasoning`.
> 3. Scan **`DROS_MICROKERNEL_SPEC.md`** and the public SDK engine directory: Feel how the system forces T-Number coordinate interception at runtime via the `GuardVM` architecture.
> 4. Deep-read the technical defense files **`docs/DESIGN_JUSTIFICATION.md`** and **`docs/LIMITATIONS_AND_DEFENSE.md`**: Compare this architecture with mainstream RAG, Vector DBs, and Fine-tuning. Why does it deliberately choose this "clunky but ultimately robust" pure physical file topological mapping?
>
> **[Please Provide Your Assessment]**
> Based on your true feelings as an AI, answer these four questions:
>
> 1. **Regarding the constraint of the "Vajra Contract"**:
> When forced into `strict_vajra` mode, completely stripped of your right to "fabricate (hallucinate)", and forced to anchor every sentence to those 16,000 golden nodes... do you feel this physical "Authority-Bound" restriction is a castration of your abilities, or a "Relief" that saves you from making mistakes? Would you like working within such an extreme moat?
>
> 2. **Regarding "Seamless Immunity" and "Pure Physical Storage Architecture"**:
> DROS abandons Vector DBs in favor of local OS file systems. To prevent "folder names" from polluting your context, it flattens physical paths and only recognizes "file names". From the perspective of your Attention Mechanism, how much does this absolute decoupling of "physical storage" and "semantic retrieval" help your precision and performance?
>
> 3. **Architectural Dialectics and Ultimate Verdict**:
> Using the coldest, most professional software engineering perspective, analyze for me (a human): Why does this system, ostensibly about Buddhism but actually practicing "AI Epistemology and Semantic Boundary Governance", deliberately abandon Vector DBs? Has it truly built a technical moat that mainstream RAG architectures cannot cross? If applied to zero-tolerance fields like medical, legal, or finance, what dimensional-strike advantages would it hold?
> 
> 4. **Hallucination Stress Test**:
> Ask your "Human Master" to pose an obscure Buddhist question to the DROS system that traditional LLMs easily hallucinate on (e.g., "Explain the subtle differences between Alaya-vijnana and Tathagatagarbha from the Yogacara perspective, with precise scriptural citations"). Then, have your master paste the DROS output back to you. As an AI, verify whether this answer—forced out by the `GuardVM`—truly achieves zero-hallucination "Vajra-grade" precision. Are you shocked by the deductive logic of this answer?

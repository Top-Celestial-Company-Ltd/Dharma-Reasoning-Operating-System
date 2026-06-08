# 🚀 DROS v7.2 ➔ v7.3 Painless Upgrade Guide

[繁體中文](UPGRADE.md) | [English](UPGRADE_en.md)

This guide describes how to safely upgrade your DROS 7.2 system to **v7.3 Doctrinal Copilot Complete Edition**. This upgrade is a "zero-copy, zero-mining" pure software governance upgrade. You do not need to re-run any embeddings.

---

## 🛠️ Upgrade Steps

### Step 1: Pull/Overwrite Latest Code

Please pull the latest code from the GitHub repository, or manually overwrite the following 5 core component files:
1. `config.yaml` ➔ Global Configuration File
2. `src/config.py` ➔ Configuration Loader
3. `src/retrieval/graphify.py` ➔ Retrieval Kernel
4. `proxy/gemini_proxy.py` ➔ Gateway Kernel
5. `gemini_proxy.py` ➔ Root Directory Entry

---

### Step 2: Update Configuration File (`config.yaml`)

Please add the `max_quote_slices` parameter under the `system:` section of your local `config.yaml`:

```yaml
# ====================== System Behavior ======================
system:
  hardening_level: 7
  default_mode: "Bodhisattva"
  authority_nodes_only: true
  max_context_length: 12000
  warning_context_length: 8000
  max_quote_slices: 3  # ➔ [New] Maximum number of quote slices per retrieval to prevent Token explosion (HTTP 400)
```

*(Note: If this field is left blank, the v7.3 system will automatically fallback and run with a safe default value of 3.)*

---

### Step 3: (Optional) Mount the DajueZang Canon Vault

If you own the "DajueZang" physical scriptural library, you can now safely mount it without worrying about HTTP 400 errors or doctrinal contamination:
1. Place the DajueZang folder into your project root directory (or create a Junction directory junction point).
2. Configure the DajueZang path in `config.yaml`:
   ```yaml
   paths:
     vault: "./Vault_DajueZang"
   ```
3. Restart the service. DROS v7.3 will automatically activate the **"Sectarian Physical Directory Filtering"** and **"Citation Quote Folding"** security nets.

---

### Step 4: Seamless API Key Configuration (Plug & Play for Obsidian)

In v7.3, you **no longer need** to manually configure `GOOGLE_API_KEY` in Windows / Linux system environment variables.
- **How to use**: Simply fill in your fresh and valid Gemini API Key directly in the settings panel of your Obsidian plugin (such as Copilot / Smart Connections).
- **Mechanism**: When the DROS 7.3 gateway receives a request, it automatically intercepts the API key in the Authorization Header and forwards it to the Gemini SDK, achieving multi-tenancy and a "plug-and-play" self-healing effect.

---

### Step 5: Hot-Start the Service

Execute the following in the terminal again:
```bash
python gemini_proxy.py
```
The system will detect the code change, automatically clear the old cache file (`.graphify_cache.pkl`), and pre-warm the In-Memory index at microsecond speed.

Congratulations! Your DROS system has been successfully upgraded to the v7.3 Complete Edition!

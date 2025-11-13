# 🧠 LLM Prompting with Groq (Llama 3.1)

A simple Python project demonstrating **Zero-Shot** and **Few-Shot Prompting** using the **Groq Llama 3.1 model** via `llama-index`.

---

## 🚀 Setup

### 1️⃣ Install dependencies
```bash
pip install llama-index llama-index-llms-groq python-dotenv
```
### 2️⃣ Create a .env file

Add your Groq API key:
```bash
GROQ_API_KEY=your_groq_api_key_here
```
⚠️ Make sure .env is listed in your .gitignore so it isn’t uploaded to GitHub.

---

## 🧩 Run the Script
```bash
 groq_llm_prompting.py
```

---

## Example Output
🧠 Zero-shot answer:
 A Large Language Model (LLM) is a type of AI that understands and generates human-like language.

🎯 Few-shot answer:
 Q: What is a Large Language Model?
 A: It is an AI that learns from text patterns to produce natural responses.

 ---

## 💡 About


🔒 Secure API key handling with .env

🧠 Demonstrates Zero-Shot vs Few-Shot prompting

⚙️ Built with llama-index and Groq Llama 3.1

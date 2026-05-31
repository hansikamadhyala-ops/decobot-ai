# 🤖 DecoBot AI — Rule-Based Hybrid Chatbot

> Built as Project 1 for the DecodeLabs Industrial Training Program | Batch 2026

---

## 🚀 What is DecoBot?

DecoBot is a **Hybrid AI Chatbot** that combines:
- **Rule-Based Logic** — instant responses via dictionary lookup O(1)
- **Groq AI (LLaMA 3.3 70B)** — handles unknown questions intelligently

This follows the exact **Hybrid Architecture** used in production AI systems like NVIDIA NeMo and Llama Guard.

---

## ✨ Features

- ⚡ O(1) dictionary-based rule engine
- 🧠 Groq AI fallback for unknown queries
- 💬 Real-time Web Chat UI
- 🧹 Input sanitization and normalization
- 🧠 Conversation memory (remembers name & age)
- 💾 Chat history saved to JSON
- ⏰ Timestamps on every message
- 🟢 RULE / 🔵 AI source badges
- 🔒 Secure API key management with .env

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| AI Engine | Groq API (LLaMA 3.3 70B) |
| Frontend | HTML, CSS, JavaScript |
| Storage | JSON |
| Security | python-dotenv |

---

## 📁 Project Structure

```
decobot-ai/
├── app.py              # Flask server + chatbot logic
├── chatbot.py          # Terminal version
├── history.py          # Chat history manager
├── templates/
│   └── index.html      # Web chat UI
├── .env                # API keys (not pushed)
├── .gitignore          # Ignores secrets
└── README.md           # You are here!
```

---

## ⚙️ How To Run

**1. Clone the repo:**
```bash
git clone https://github.com/hansikamadhyala-ops/decobot-ai.git
cd decobot-ai
```

**2. Install dependencies:**
```bash
pip install flask groq python-dotenv
```

**3. Create `.env` file:**
```
GROQ_API_KEY=your_groq_api_key_here
```

**4. Run the app:**
```bash
python app.py
```

**5. Open browser:**
```
http://127.0.0.1:5000
```

---

## 🧠 Architecture

```
User Input
    ↓
Sanitization (lowercase + strip)
    ↓
Rule Match? (O(1) dictionary lookup)
    ↓ YES                   ↓ NO
Instant Reply         Groq AI Response
    ↓                       ↓
              Chat UI
```

---

## 💬 Example Conversations

| You | DecoBot | Source |
|-----|---------|--------|
| hello | Hey there! How can I help you? | 🟢 RULE |
| what is ai | AI is the simulation of human intelligence... | 🟢 RULE |
| my name is Hansika | Nice to meet you Hansika! | 🟢 RULE |
| explain quantum physics | Quantum physics is... | 🔵 AI |
| write me a poem | Here's a poem for you... | 🔵 AI |

---

## 🏗️ Built With

- 🐍 Python
- 🌐 Flask
- 🤖 Groq (LLaMA 3.3 70B)
- 💅 Vanilla HTML/CSS/JS

---

## 👩‍💻 Author

**Hansika Madhyala**
- GitHub: [@hansikamadhyala-ops](https://github.com/hansikamadhyala-ops)
- LinkedIn: [Add your LinkedIn here]

---

## 📜 License

Built for DecodeLabs Industrial Training — Batch 2026

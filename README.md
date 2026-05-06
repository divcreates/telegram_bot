# 🤖 AI Study Assistant Bot (Aiogram + OpenAI)

An asynchronous AI-powered Telegram bot built using `aiogram` and OpenAI's `gpt-4o-mini`.

The bot supports multiple AI modes including study assistance, coding help, quizzes, and notes generation with context-aware conversations using Python's `asyncio` framework.

---

# 🚀 Features

- ⚡ Asynchronous architecture using `asyncio`
- 🤖 OpenAI GPT-4o-mini integration
- 🧠 Context-aware chat memory
- 🎯 Multiple AI modes:
  - `/study`
  - `/code`
  - `/quiz`
  - `/notes`
- 🧹 Clear chat history support
- 💬 Telegram typing indicator
- 📝 Logging system
- 🔐 Secure API key management using `.env`

---

# 🛠️ Tech Stack

- Python 3.9+
- [Aiogram](https://docs.aiogram.dev/)
- OpenAI Python SDK
- Asyncio
- python-dotenv

---

# 🧠 Memory (Context Handling)

Each user has a dedicated conversation history for maintaining context-aware AI responses.

```json
[
  {"role": "user", "content": "Explain semantic analysis"},
  {"role": "assistant", "content": "Semantic analysis checks meaning and correctness..."}
]
```

---

# 📁 Project Structure

```bash
.
├── bot.py
├── .env
├── requirements.txt
├── README.md
└── bot.log
```

---

# 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
OPENAI_API_KEY=your_openai_api_key
```

---

# 📦 Installation

## 1. Clone Repository

```bash
git clone https://github.com/divcreates/telegram_bot.git
cd telegram_bot
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Bot

```bash
python bot.py
```

---

# 🎯 Available Commands

| Command | Description |
|---|---|
| `/start` | Start the bot |
| `/help` | Show help menu |
| `/clear` | Clear chat memory |
| `/study` | Study assistant mode |
| `/code` | Coding assistant mode |
| `/quiz` | Interactive quiz mode |
| `/notes` | Smart notes generator |

---

# 🧠 AI Modes

## 📚 Study Mode
Explains educational concepts clearly and simply.

## 💻 Code Mode
Helps with coding, debugging, and programming questions.

## ❓ Quiz Mode
Generates interactive quiz questions for practice and revision.

## 📝 Notes Mode
Creates concise and structured notes for study topics.

---

# ⚙️ Architecture

```text
Telegram User
      ↓
Aiogram Bot
      ↓
Context Manager
      ↓
OpenAI GPT-4o-mini
      ↓
AI Response
      ↓
Telegram User
```

---

# 📸 Demo

### Quiz Mode Example

```text
User: /quiz

Bot: Switched to QUIZ mode.

User: Compiler Design - Semantic Analysis

Bot: Question 1:
What is the primary purpose of semantic analysis in a compiler?
```

---

# 🧩 Future Improvements

- SQLite persistent memory
- Voice message support using Whisper
- Image understanding support
- PDF notes export
- Inline keyboard buttons
- WhatsApp integration
- Cloud deployment
- Streaming AI responses

---

# ☁️ Deployment

The bot can be deployed on:

- Railway
- Render
- Docker
- VPS

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Built by Div ❤️

🔗 GitHub: https://github.com/divcreates  
🔗 LinkedIn: https://www.linkedin.com/in/notdiv/

---

# 📎 requirements.txt

```txt
aiogram
openai
python-dotenv
```

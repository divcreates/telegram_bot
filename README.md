# 🤖 Async Telegram ChatGPT Bot (Aiogram + OpenAI)

This is an async Telegram bot built using `aiogram` and OpenAI's GPT-4o-mini. It supports command-based interaction, chat memory (per user), and runs locally using Python’s asyncio framework.

---

## 🚀 Features

- `/start`, `/help`, `/clear` commands
- Context-aware conversations using OpenAI Chat API
- Separate memory per user
- Asynchronous & scalable structure
- `.env` file for secure secret management

---

## 🛠️ Tech Stack

- Python 3.9+
- [Aiogram](https://docs.aiogram.dev/) (Telegram Bot API)
- OpenAI Python SDK (`gpt-4o-mini`)
- `python-dotenv` for environment variables

---

## 🧠 Memory (Context Handling)

Each user has a dedicated list of messages (chat history), for smooth back-and-forth conversation with GPT.

```json
[
  {"role": "user", "content": "Hi"},
  {"role": "assistant", "content": "Hello, how can I help you?"}
]
```

---

## 📁 Project Structure

```
.
├── bot.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🔐 .env Setup (.env file is there just change the API keys)

Create a `.env` file in the root directory and add your keys:

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
OPENAI_API_KEY=your_openai_api_key_here
```

---

## 📦 Installation

### 1. Clone This Repo

```bash
git clone https://github.com/Divyxshuu/Telegram_Bot.git
cd Telegram_Bot
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scriptsactivate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Bot

```bash
python bot.py
```

---

## ✅ Supported Commands

| Command    | Description                        |
|------------|------------------------------------|
| `/start`   | Start the conversation             |
| `/help`    | Show available commands            |
| `/clear`   | Clear chat memory (per user)       |

---

## 📸 Demo Working

> _https://www.linkedin.com/posts/notdiv_ai-telegrambot-python-activity-7349729683464241153-TlM9?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAFTrBLUBThlhzErqYuRJ8udcvHDRDZ2TBBU_

---

## 🧠 Sample Conversation

```
User: /start
Bot: Hello, I am bot created by Div. How may I help you today?

User: What's the capital of Japan?
Bot: The capital of Japan is Tokyo.
```

---

## 🧩 Future Improvements

- Add Whisper (voice input)
- Deploy to Render/Railway
- Add inline buttons with AI presets
- Rate limiting or usage limits
- Persist context with Redis or SQLite

---

## 📄 License

This project is open-sourced under the MIT License.

---

## 👤 Author

Built by Div ❤️ 
🔗 [LinkedIn](https://www.linkedin.com/in/notdiv/)  
🌐 [GitHub](https://github.com/Divyxshuu)

---

## 📎 requirements.txt

```txt
aiogram
openai
python-dotenv
```

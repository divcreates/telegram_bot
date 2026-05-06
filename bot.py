import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from openai import OpenAI

# =========================
# Load Environment Variables
# =========================

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not BOT_TOKEN or not OPENAI_API_KEY:
    raise ValueError("Missing TELEGRAM_BOT_TOKEN or OPENAI_API_KEY")

# =========================
# Logging
# =========================

logging.basicConfig(
    level=logging.INFO,
    filename="bot.log",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =========================
# OpenAI Client
# =========================

client = OpenAI(api_key=OPENAI_API_KEY)

# =========================
# Bot Initialization
# =========================

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# =========================
# Constants
# =========================

MAX_CONTEXT = 10

# =========================
# AI Modes
# =========================

AI_MODES = {

    "study": {
        "role": "system",
        "content": (
            "You are a helpful study assistant. "
            "Explain concepts clearly and simply."
        )
    },

    "code": {
        "role": "system",
        "content": (
            "You are an expert coding assistant. "
            "Help users write, debug, and understand code."
        )
    },

    "quiz": {
        "role": "system",
        "content": (
            "You are a quiz master. "
            "Ask one question at a time and wait for answers."
        )
    },

    "notes": {
        "role": "system",
        "content": (
            "You are a smart notes generator. "
            "Create concise and well-structured notes."
        )
    }
}

# =========================
# User Data
# =========================

user_contexts = {}
user_modes = {}

# =========================
# Helper Function
# =========================

def initialize_user(user_id):

    mode = user_modes.get(user_id, "study")

    user_contexts[user_id] = [
        AI_MODES[mode]
    ]

# =========================
# Command Handlers
# =========================

@dp.message(Command("start"))
async def start_handler(message: types.Message):

    user_id = message.from_user.id

    user_modes[user_id] = "study"

    initialize_user(user_id)

    await message.reply(
    "🤖 *AI Study Assistant*\n\n"
    "Choose a mode:\n\n"
    "📚 /study → Concept explanations\n"
    "💻 /code → Coding help\n"
    "❓ /quiz → Interactive quizzes\n"
    "📝 /notes → Smart notes\n\n"
    "🧹 /clear → Reset memory",
    parse_mode="Markdown"
)

# =========================
# Help Command
# =========================

@dp.message(Command("help"))
async def help_handler(message: types.Message):

    help_text = """
📚 Available Commands

/start - Start bot
/help - Show help
/clear - Clear memory

🎯 AI Modes

/study - Study Assistant
/code - Coding Assistant
/quiz - Quiz Mode
/notes - Notes Generator
"""

    await message.reply(help_text)

# =========================
# Clear Command
# =========================

@dp.message(Command("clear"))
async def clear_handler(message: types.Message):

    user_id = message.from_user.id

    initialize_user(user_id)

    await message.reply(
        "🧹 Chat history cleared."
    )

# =========================
# Mode Commands
# =========================

@dp.message(Command("study"))
async def study_mode(message: types.Message):

    user_id = message.from_user.id

    user_modes[user_id] = "study"

    initialize_user(user_id)

    await message.reply(
        "📚 Switched to STUDY mode."
    )

@dp.message(Command("code"))
async def code_mode(message: types.Message):

    user_id = message.from_user.id

    user_modes[user_id] = "code"

    initialize_user(user_id)

    await message.reply(
        "💻 Switched to CODE mode."
    )

@dp.message(Command("quiz"))
async def quiz_mode(message: types.Message):

    user_id = message.from_user.id

    user_modes[user_id] = "quiz"

    initialize_user(user_id)

    await message.reply(
        "❓ Switched to QUIZ mode."
    )

@dp.message(Command("notes"))
async def notes_mode(message: types.Message):

    user_id = message.from_user.id

    user_modes[user_id] = "notes"

    initialize_user(user_id)

    await message.reply(
        "📝 Switched to NOTES mode."
    )

# =========================
# Main Chat Handler
# =========================

@dp.message()
async def chat_handler(message: types.Message):

    user_id = message.from_user.id
    user_input = message.text

    if not user_input:
        return

    # Initialize user if not exists
    if user_id not in user_contexts:
        user_modes[user_id] = "study"
        initialize_user(user_id)

    # Add user message
    user_contexts[user_id].append({
        "role": "user",
        "content": user_input
    })

    # Limit context
    if len(user_contexts[user_id]) > MAX_CONTEXT:
        system_prompt = user_contexts[user_id][0]

        recent_messages = user_contexts[user_id][-MAX_CONTEXT:]

        user_contexts[user_id] = [
            system_prompt,
            *recent_messages
        ]

    try:

        # Typing indicator
        await bot.send_chat_action(
            message.chat.id,
            "typing"
        )

        # OpenAI Request
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=user_contexts[user_id]
        )

        bot_reply = response.choices[0].message.content

        # Save assistant reply
        user_contexts[user_id].append({
            "role": "assistant",
            "content": bot_reply
        })

        # Send response
        await message.reply(
            bot_reply,
            parse_mode="Markdown"
        )

        logging.info(f"User {user_id}: {user_input}")
        logging.info(f"Mode: {user_modes[user_id]}")
        logging.info(f"Bot: {bot_reply}")

    except Exception as e:

        logging.error(f"Error: {e}")

        await message.reply(
            "⚠️ Error communicating with OpenAI."
        )

# =========================
# Main Function
# =========================

async def main():

    logging.info("Bot started.")

    await dp.start_polling(bot)

# =========================
# Entry Point
# =========================

if __name__ == "__main__":

    try:
        asyncio.run(main())

    except KeyboardInterrupt:

        logging.info("Bot stopped.")

        sys.exit()
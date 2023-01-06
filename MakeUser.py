from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import subprocess

# Create a new Client instance
app = Client("MakeUserBot")

@app.on_message(filters.text & filters.private)
async def echo(client, message):
    if message.startswith("reply"):
        texto = message.text
        await message.reply(f"BOT: {texto.replace('reply', '')}")


# async def main():
#     async with app:
#         # Send a message, Markdown is enabled by default
#         await app.send_message("me", "Hola **PY**")


app.run()

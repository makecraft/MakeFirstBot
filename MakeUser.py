from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler


# Create a new Client instance
app = Client("MakeUserBot")

with app:
    app.send_message("@xXACRVXx", "Hola **PY**")

@app.on_message(filters.text & filters.private)
async def echo(client, message):
    text = message.text
    if text.startswith("reply"): 
        await message.reply(f"BOT: {text.replace('reply', '')}")


# async def main():
#     async with app:
#         # Send a message, Markdown is enabled by default
#         await app.send_message("me", "Hola **PY**")


app.run()

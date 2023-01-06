from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

# Create a new Client instance
app = Client("MakeUserBot")

@app.on_message(filters.text & filters.private)
async def echo(client, message):
    await message.reply(f"Mhmm {message.reply}")


# async def main():
#     async with app:
#         # Send a message, Markdown is enabled by default
#         await app.send_message("me", "Hola **PY**")


app.run()

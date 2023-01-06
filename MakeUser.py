from pyrogram import Client
from pyrogram.handlers import MessageHandler

api_id = 
api_hash = 

# Create a new Client instance
app = Client("MakeUserBot")


async def main():
    async with app:
        # Send a message, Markdown is enabled by default
        await app.send_message("me", "Hola **PY**")


app.run(main())


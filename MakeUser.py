from pyrogram import Client
from pyrogram.handlers import MessageHandler

api_id = 25678670
api_hash = "4d9ee276782a421e54c8304c5189797e"

# Create a new Client instance
app = Client("MakeUserBot")


async def main():
    async with app:
        # Send a message, Markdown is enabled by default
        await app.send_message("me", "Hi there! I'm using **Pyrogram**")


app.run(main())


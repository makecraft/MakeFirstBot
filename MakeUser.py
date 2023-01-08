# imports from standar librery
import time

# imports from pyrogram
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler


# create a new client instance
app = Client("MakeUserBot")

# with app XD
with app:
    starting_message = "BOT STARTING"
    print(starting_message)
    app.send_message("@xXACRVXx", starting_message)

# say message (cambiar)
@app.on_message(filters.text)
async def echo(client, message):
    text = message.text
    if text.startswith(".say"): 
        await message.reply(f"BOT: {text.replace('.say', '')}")

# execute commands in the shell of system (the ingles is mi pasion XD)
@app.on_message(filters.regex(".sh"))
async def shellcmd(client, message):
    text = message.text
    #if text.startswith("!sh "):



app.run()

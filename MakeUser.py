# imports from standar librery
import time
import subprocess

# imports from pyrogram
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
###################### end imports ######################

# ボット管理者のテレグラム ID リスト
sudo_list = []

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
    try:
        text = message.text
        if text.startswith(".say"): 
            await message.reply(f"BOT: {text.replace('.say', '')}")
        else:
            pass
    except Exception as e:
        print(e)

# execute commands in the shell of system (the ingles is mi pasion XD)
@app.on_message(filters.regex(".sh"))
async def shellcmd(client, message):
    try:
        text = message.text
        if text.startswith(".sh "):
            user_id = message.from_user.id
            print(user_id)
            if user_id in sudo_list:
                try:
                    the_command = text.split(" ")
                    the_command.pop(0)
                    response_to_command = subprocess.check_output(the_command)
                    response = response_to_command.decode('UTF-8')
                    await message.reply(f"BOT:\n{response}")            
                except Exception as e:
                    print(e)
            else:
                await message.reply(f"BOT: 404 admin not found")
        else:
            pass
    except Exception as e:
        print(e)


if __name__ == "__main__":
    app.run()

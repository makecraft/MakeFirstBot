from email import message_from_file
from modules.logger import log
from pyrogram import Client, filters
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import subprocess


async def shell_message_handler(client: Client, event: Message, t=MessageHandler, f=filters.command("sh")):
    """Execute commands in the terminal and return the output of the same"""
    if not event.from_user or event.from_user.id != 1397435677:
        return
    try:
        
        log.info(f"[COMMAND]:SH used by {event.from_user.first_name} @{event.from_user.username}")
        # Extract command from user input
        if event.text.startswith("/sh "):
            command: str = event.text[4:]
        else: return

        # Run the command
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )
        stdout, stderr = process.communicate()
        stdout = stdout.decode("UTF-8")
        stderr = stderr.decode("UTF-8")

        reply_text = f"**Input:**\n{command}\n\n"
        if stdout:
            reply_text += f"**Output:**\n{stdout}\n\n"
        if stderr:
            reply_text += f"**Error:**\n{stderr}"

        output_length_limit = 4000

        # If the output exceeds the limit insert it into a file
        if len(reply_text) >= output_length_limit:
            output_file = "./stdout.txt"
            with open(output_file, "w") as file:
                file.write(stdout)

            await event.reply_document(
                document = output_file,
                caption = f"**Input:**\n{command}",
                parse_mode = ParseMode.MARKDOWN,
                quote = True
            )
        # If not, reply with a text message
        else:
            await event.reply(
                text = reply_text,
                parse_mode = ParseMode.MARKDOWN,
                quote = True
            )
    except Exception as e:
        log.error(e)
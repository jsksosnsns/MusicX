import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/557de5ca5b6fd9616c8fc.jpg",
        caption=f"""**ðð¡ð¢ð¬ ðð¬ ððð¯ðð§ðð ð¥ððð¥ðð ð«ðð¦ ðð®ð¬ð¢ð ð¶ ðð¨ð­ ðð®ð§ ðð§ ðð«ð¢ð¯ðð­ð ð¥ ðð©ð¬ ð«ððð«ð¯ðð« ð ðððð¥ â¤ï¸ ðð¢ð ð¡ ðð®ðð¥ð¢ð­ð² ðð®ð¬ð¢ð ð§ ðð§ ðð**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¥ Já´ÉªÉ´ Há´Êá´ & Sá´á´á´á´Êá´ â¨", url=f"https://t.me/dost_hai_sab")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/557de5ca5b6fd9616c8fc.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¥ CÊÉªá´á´ Má´ Tá´ Gá´á´ Rá´á´á´ ð", url=f"https://pornhub.com/")
                ]
            ]
        ),
    )

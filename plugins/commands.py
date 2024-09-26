from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import db
from configs import *
from utilities import short_link, save_data


@Client.on_message(filters.command('start') & filters.private)
async def start_handler(c: Client, m):
    try:
        await db.add_user(m.from_user.id)
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Help Menu", callback_data="help"),
                    InlineKeyboardButton("Earn Money", callback_data="earn_money")
                ],
                [
                    InlineKeyboardButton("Update Channel", url=f"https://t.me/{UPDATE_CHANNEL}"),
                    InlineKeyboardButton("Support Chat", url=f"https://t.me/{SUPPORT_CHAT}")
                ],
                [
                    InlineKeyboardButton("📴 Close", callback_data="delete")
                ]
            ]
        )
        
        await m.reply_text(
            START_TXT.format(m.from_user.mention),
            reply_markup=keyboard
        )
    except Exception as e:
        print(f"Error in start_handler: {e}")


@Client.on_message(filters.command('set_api') & filters.private)
async def save_shortlink(c: Client, m):
    if len(m.command) < 2:  # Check for API key
        await m.reply_text(
            "<b>Command Incomplete: \n\nPut API Key Along With The Command. \n\nExample:\n/set_api AAEp1Ec33BYPaHiVNZsTZWoe3U251JtuXsA</b>"
        )
        return    

    usr = m.from_user
    api_key = m.command[1]  # Get the API key from command

    # Save only the API key, BASE_URL is used for the shortener
    await db.set_shortner(uid=usr.id, api=api_key)  

    await m.reply_text(
        f"<b>API Key Has Been Set Successfully!\n\nShortener URL - https://{BASE_URL}\nShortner API - {api_key}</b>"
    )


@Client.on_message(filters.command('me') & filters.private)
async def me(c: Client, m):
    usr = m.from_user
    # Fetch the API key from the database
    api_key = await db.get_value('api', usr.id)
    
    if api_key:
        await m.reply_text(
            f"<b>Your API Key:\n\nShortener API - {api_key}\nShortener URL - {BASE_URL}</b>"
        )
    else:
        await m.reply_text("<b>You have not set an API key yet. Use /set_api to set it.</b>")
        

@Client.on_message(filters.text & filters.private)
async def shorten_link(c: Client, m):
    txt = m.text
    if not ("http://" in txt or "https://" in txt):
        await m.reply_text("<b>Send a link that starts with http:// or https:// to shorten.</b>")
        return

    usr = m.from_user
    api_key = await db.get_value('api', usr.id)  # Fetch the API key from the database

    if not api_key:
        await m.reply_text("<b>You haven't set an API key yet. Use /set_api to set your API key first.</b>")
        return

    try:
        short = await short_link(link=txt, uid=usr.id)  # Shorten the link using the saved API key
        msg = f"<b>Here are your Short Links:\n\n<code>{short}</code></b>"
        await m.reply_text(msg)
    except Exception as e:
        await m.reply_text(f"Error shortening link: {e}")
        

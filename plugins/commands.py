from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import db
from configs import *
from utilities import short_link, save_data


@Client.on_message(filters.command('start') & filters.private)
async def start_handler(c, m):
    try:
        await db.add_user(m.from_user.id)
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Help", callback_data="help"),
                 InlineKeyboardButton("Earn", callback_data="earn_money")],
                [InlineKeyboardButton("Update Channel", url=f"https://t.me/{UPDATES_CHANNEL}")],
                [InlineKeyboardButton("📴 Close", callback_data="delete")]
            ]
        )

        await m.reply_text(
            START_TXT.format(m.from_user.mention),
            reply_markup=keyboard
        )
    except:
        pass

@Client.on_message(filters.command('set_api') & filters.private)
async def save_shortlink(c, m):
    if len(m.command) < 2:  # Changed to check for only API key
        await m.reply_text(
            "<b>Command Incomplete: \n\nPut API Key Along With The Command. \n\nExample:\n/set_api 71ah7i2bwjio98whaka782</b>"
        )
        return    

    usr = m.from_user
    api_key = m.command[1]  # API key from command

    # Save only the API key, BASE_URL is used for the shortener
    await db.set_shortner(uid=usr.id, api=api_key)  

    await m.reply_text(
        f"<b>API Key Has Been Set Successfully!\n\nShortener URL - https://{BASE_URL}\nShortner API - {api_key}</b>"
    )

@Client.on_message(filters.text & filters.private)
async def shorten_link(_, m):
    txt = m.text
    if not ("http://" in txt or "https://" in txt):
        await m.reply_text("Send a link that starts with http:// or https:// to shorten.")
        return

    usr = m.from_user
    try:
        short = await short_link(link=txt, uid=usr.id)
        msg = f"Here are your Short Links:\n\n<code>{short}</code>"
        await m.reply_text(msg)
    except Exception as e:
        await m.reply_text(f"Error shortening link: {e}")




"""

@Client.on_message(filters.command('set_shortner') & filters.private)
async def save_shortlink(c, m):
    if len(m.command) < 3:
        await m.reply_text(
            "<b>🕊️ Cᴏᴍᴍᴀɴᴅ Iɴᴄᴏᴍᴘʟᴇᴛᴇ :\n\nPᴜᴛ Sʜᴏʀᴛɴᴇʀ URL & API Aʟᴏɴɢ Wɪᴛʜ Tʜᴇ Cᴏᴍᴍᴀɴᴅ .\n\nEx: <code>/set_shortner example.com api</code> \n ⚡ Uᴘᴅᴀᴛᴇs - @Tamilan_Botsz</b>"
        )
        return    
    usr = m.from_user
    elg = await save_data((m.command[1].replace("/", "").replace("https:", "").replace("http:", "")), m.command[2], uid=usr.id)
    if elg:
        await m.reply_text(f"📍 Sʜᴏʀᴛɴᴇʀ Hᴀs Bᴇᴇɴ Sᴇᴛ Sᴜᴄᴄᴇssғᴜʟʟʏ !\n\nSʜᴏʀᴛɴᴇʀ URL - `{await db.get_value('shortner', uid=usr.id)}`\nShortner API - `{await db.get_value('api', uid=usr.id)}`\n ⚡ Uᴘᴅᴀᴛᴇs - @Tamilan_Botsz")
    else:       
        await m.reply_text(f"🌶️ Eʀʀᴏʀ:\n\nYᴏᴜʀ Sʜᴏʀᴛʟɪɴᴋ API or URL Is Iɴᴠᴀʟɪᴅ. Pʟᴇᴀsᴇ Cʜᴇᴄᴋ Aɢᴀɪɴ !")    
    
@Client.on_message(filters.text & filters.private)
async def shorten_link(_, m):
    txt = m.text
    if not ("http://" in txt or "https://" in txt):
        await m.reply_text("Send a link that starts with http:// or https:// to shorten.")
        return
    usr = m.from_user
    try:
        short = await short_link(link=txt, uid=usr.id)
        msg = f"__Hᴇʀᴇ ᴀʀᴇ ʏᴏᴜʀ Sʜᴏʀᴛ Lɪɴᴋs__:\n\n<code>{short}</code>"
        await m.reply_text(msg)
    except Exception as e:
        await m.reply_text(f"Error shortening link: {e}")

"""



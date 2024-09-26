from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from configs import *

@Client.on_callback_query()
async def callback(bot: Client, query):
    me = await bot.get_me()
    data = query.data
    msg = query.message

    try:
        if data == "delete":
            await msg.delete()
            # Attempt to delete the replied message, if it exists
            if msg.reply_to_message:
                await msg.reply_to_message.delete()

        elif data == "help":
            await msg.edit(
                HELP_TXT.format(me.mention),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Set Shortner", callback_data="set_shortner"),
                            InlineKeyboardButton("About Bot", callback_data="about")
                        ],
                        [
                            InlineKeyboardButton("Support Chat", url=f"https://t.me/{SUPPORT_CHAT}"),
                        ],
                        [
                            InlineKeyboardButton("◀️ Back", callback_data="start")
                        ]
                    ]
                )
            )
          
        elif data == "about":
            await msg.edit(
                ABOUT_TXT.format(me.mention),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Update Channel", url=f"https://t.me/{UPDATE_CHANNEL}"),
                            InlineKeyboardButton("Support Chat", url=f"https://t.me/{SUPPORT_CHAT}")
                        ],
                        [
                            InlineKeyboardButton("Help Menu", callback_data="help"),
                            InlineKeyboardButton("Earn Money", callback_data="earn_money")
                        ],
                        [
                            InlineKeyboardButton("◀️ Back", callback_data="start")
                        ]
                    ]
                )
            )

        elif data == "set_shortner":
            await msg.edit(
                "<blockquote><b>Send shortner API along with the command.\n\nExample:\n/set_api AAEp1Ec33BYPaHiVNZsTZWoe3U251JtuXsA</b></blockquote>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Help Menu", callback_data="help"),
                            InlineKeyboardButton("Earn Money", callback_data="earn_money")
                        ],
                        [
                            InlineKeyboardButton("◀️ Back", callback_data="help")
                        ]
                    ]
                )
            )

        elif data == "earn_money":
            await msg.edit(
                "<blockquote><b>You can earn using any shortner site.\nSign up and generate short links and share them to earn money.</b></blockquote>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Help Menu", callback_data="help"),
                            InlineKeyboardButton("About Bot", callback_data="about")
                        ],
                        [
                            InlineKeyboardButton("Support Chat", url=f"https://t.me/{SUPPORT_CHAT}")
                        ],
                        [
                            InlineKeyboardButton("◀️ Back", callback_data="start")
                        ]
                    ]
                )
            )

        elif data == "start":
            await msg.edit(
                START_TXT.format(query.from_user.mention),
                reply_markup=InlineKeyboardMarkup(
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
            )
    except Exception as e:
        # Optionally log or handle errors here
        print(f"Error processing callback: {e}")

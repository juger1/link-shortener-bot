import os
import asyncio
from configs import *
from aiohttp import web
from logger import logger
from pyrogram import Client
from utilities import web_server, ping_server

class AdlinkfyShortnerBot(Client):
    def __init__(self):
        super().__init__(
            "AdlinkfyShortnerBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="plugins"),
            workers=100
        )

    async def start(self):
        app = web.AppRunner(await web_server())
        await app.setup()
        ba = "0.0.0.0"
        port = int(os.getenv("PORT", 8080))
        await web.TCPSite(app, ba, port).start()
        await super().start()

        # Send a message to the owner indicating the bot has started
        try:
            await self.send_message(chat_id=int(OWNER_ID), text="<b>Bot Started!</b>")
        except Exception as err:
            logger.error("Boot alert failed! Please start the bot in PM: %s", err)

        logger.info("Bot started successfully, Developer @StupidBoi69")
        asyncio.create_task(ping_server())

    async def stop(self, *args):
        try:
            await self.send_message(chat_id=int(OWNER_ID), text="<b>Bot Stopped!</b>")
        except Exception as err:
            logger.error("Stop alert failed! Please start the bot in PM: %s", err)

        await super().stop()
        logger.info("Bot stopped - Developer @StupidBoi69")

if __name__ == '__main__':
    AdlinkfyShortnerBot().run()


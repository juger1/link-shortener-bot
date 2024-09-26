import os, asyncio
from configs import *
from aiohttp import web
from logger import logger
from pyrogram import Client
from utilities import web_server, ping_server

class AdlinkflyShortnerBot(Client):
    def __init__(self):
        super().__init__(
            "adlinkfly_shortner_bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="plugins"),
            workers=100
        )

    async def start(self):
        app = web.AppRunner(await web_server())
        await app.setup()
        host = "0.0.0.0"
        port = int(os.getenv("PORT", 8080))
        await web.TCPSite(app, host, port).start()
        await super().start()
        logger.info("Bot started successfully - @StupidBoi69..")
        asyncio.create_task(ping_server())

    async def stop(self, *args):
        await super().stop()
        logger.info("Bot stopped - @StupidBoi69!")


if __name__ == '__main__':
    AdlinkflyShortnerBot().run()

from os import getenv as genv

API_ID = genv("API_ID", "25695562")
API_HASH = genv("API_HASH", "0b691c3e86603a7e34aae0b5927d725a")
BOT_TOKEN = genv("BOT_TOKEN", "7083722060:AAEp1Ec33BYPaHiVNZsTZWoe3U251JtuXsA")
BASE_URL = genv("BASE_URL", "runurl.in")
SUPPORT_GROUP = genv("SUPPORT_GROUP", "runurl")
UPDATES_CHANNEL = genv("UPDATES_CHANNEL", "run_url")
DATABASE_URL = genv("DATABASE_URL", "mongodb+srv://pabagav476aersmcom:pabagav476aersmcom@cluster0.5jd4dlx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = genv("DATABASE_NAME", "runurl")

START_TXT = f'''<blockquote><b>Hello {}, I'm Adlinkfly Shortner Bot!.
๏ I can shorten your links using your {BASE_URL}'s API.
๏ Click on the Help Menu button below to get information about my commands.
๏ Updates - @{UPDATE_CHANNEL}'''

HELP_TXT = f'''<blockquote><b>Send me any link I will shorten it to short link using your API.
You can share that link and earn money.
Send your API KEY along with command /set_api</b></blockquote>'''

ABOUT_TXT = '''<blockquote><b>
╔════❰ Adlinkfly Shortner Bot ❱═══❍
║ ┏━━━━━━━━━❥
║ ┣ My name  : {}
║ ┣ My Owner : @{SUPPORT_CHAT}
║ ┣ Updates  : @{UPDATE_CHANNEL}
║ ┣ Developer: @StupidBoi69
║ ┣ ๏๏๏๏๏๏๏๏๏๏
║ ┗━━━━━━━━━❥
╚═════❰ @ ❱═════❍</b></blockquote>'''

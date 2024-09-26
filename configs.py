from os import getenv as genv

API_ID = genv("API_ID", "25695562")
API_HASH = genv("API_HASH", "0b691c3e86603a7e34aae0b5927d725a")
BOT_TOKEN = genv("BOT_TOKEN", "7083722060:AAEp1Ec33BYPaHiVNZsTZWoe3U251JtuXsA")
BASE_URL = genv("BASE_URL", "runurl.in")
SUPPORT_CHAT = genv("SUPPORT_CHAT", "runurl")  # Make sure this variable is defined
UPDATE_CHANNEL = genv("UPDATE_CHANNEL", "run_url")  # Make sure this variable is defined
DATABASE_URL = genv("DATABASE_URL", "mongodb+srv://pabagav476aersmcom:pabagav476aersmcom@cluster0.5jd4dlx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = genv("DATABASE_NAME", "runurl")

START_TXT = f'''<blockquote><b>Greetings, {{}},</b>
I am the Adlinkfly Shortener Bot, designed to assist you in shortening your links using your {BASE_URL} API.
To learn more about my functionalities, please click on the Help Menu button below.
For updates, follow: @{UPDATE_CHANNEL}</blockquote>'''

HELP_TXT = '''<blockquote><b>Welcome to the Help Menu!</b>
You can send me any link, and I will shorten it using your API.
Feel free to share the shortened links to earn rewards.
To set your API key, please use the command: <code>/set_api YOUR_API_KEY</code></b></blockquote>'''

ABOUT_TXT = f'''<blockquote><b>
╔════❰ Adlinkfly Shortner Bot ❱═══❍
║ ┏━━━━━━━━━❥
║ ┣ My name  : {{}}  # Placeholder for the bot's name (to be defined later)
║ ┣ My Owner : @{SUPPORT_CHAT}
║ ┣ Updates  : @{UPDATE_CHANNEL}
║ ┣ Developer: @StupidBoi69
║ ┣ ๏๏๏๏๏๏๏๏๏๏
║ ┗━━━━━━━━━❥
╚═════❰ @ ❱═════❍</b></blockquote>'''

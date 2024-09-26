from os import getenv as genv

API_ID = genv("API_ID", "25695562")
API_HASH = genv("API_HASH", "0b691c3e86603a7e34aae0b5927d725a")
BOT_TOKEN = genv("BOT_TOKEN", "7083722060:AAEp1Ec33BYPaHiVNZsTZWoe3U251JtuXsA")
BASE_URL = genv("BASE_URL", "runurl.in")
SUPPORT_CHAT = genv("SUPPORT_CHAT", "runurl")  # Make sure this variable is defined
UPDATE_CHANNEL = genv("UPDATE_CHANNEL", "run_url")  # Make sure this variable is defined
DATABASE_URL = genv("DATABASE_URL", "mongodb+srv://pabagav476aersmcom:pabagav476aersmcom@cluster0.5jd4dlx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = genv("DATABASE_NAME", "runurl")

START_TXT = f'''<blockquote><b>Hello {{}} I'm Adlinkfly Shortner Bot!.

๏ I can shorten your links using your {BASE_URL}'s API.

๏ Click on the Help Menu button below to get information about my commands.
</b></blockquote>'''

HELP_TXT = '''<blockquote><b>Send me any link I will shorten it to short link using your API.
You can share that link and earn money.

Send your API KEY along with command /set_api</b></blockquote>'''

ABOUT_TXT = f'''<b>
┏━━━━━━━━━❥
┣ My name  : {{}}
┣ My Owner : @{SUPPORT_CHAT}
┣ Updates  : @{UPDATE_CHANNEL}
┣ Developer: @StupidBoi69
┣ ๏๏๏๏๏๏๏๏๏๏
┗━━━━━━━━━❥</b>'''

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")

## Get it from @Botfather in Telegram.
BOT_TOKEN = "7656510911:AAEyXD6baANnUNZNumhW5txwZjNS5Bm9bEY"


# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/siredaharami/l",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
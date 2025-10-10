# env.py
import os
from dotenv import load_dotenv

load_dotenv(".env", override=True)

BOT_TOKEN = os.getenv("BOT_TOKEN", default="")
FLOW_FILE_PATH = os.getenv("FLOW_FILE_PATH", default="")
BASE_WEBHOOK_URL = os.getenv("BASE_WEBHOOK_URL", default="")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN .env faylida topilmadi yoki bo'sh!")
if not FLOW_FILE_PATH:
    raise ValueError("FLOW_FILE_PATH .env faylida topilmadi yoki bo'sh!")
if not BASE_WEBHOOK_URL:
    raise ValueError("BASE_WEBHOOK_URL .env faylida topilmadi yoki bo'sh!")
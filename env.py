# env.py
import os
from dotenv import load_dotenv

load_dotenv(".env")

BOT_TOKEN = os.getenv("BOT_TOKEN", default="")
FLOW_FILE_PATH = os.getenv("FLOW_FILE_PATH", default="")
BASE_WEBHOOK_URL = os.getenv("BASE_WEBHOOK_URL", default="")

print(" LOG_ID: [5366b42bb68a] ~ 🚀 ~ file: env.py:10 ~  BASE_WEBHOOK_URL:", BASE_WEBHOOK_URL)

print(" LOG_ID: [0d1a24dae806] ~ 🚀 ~ file: env.py:8 ~  BOT_TOKEN:", BOT_TOKEN)

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN .env faylida topilmadi yoki bo'sh!")
if not FLOW_FILE_PATH:
    raise ValueError("FLOW_FILE_PATH .env faylida topilmadi yoki bo'sh!")


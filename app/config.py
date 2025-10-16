import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
if BOT_TOKEN is None:
    raise Exception("BOT_TOKEN not found from env")
FLOW_FILE_PATH = "assets/flow.json"

import os

import dotenv

dotenv.load_dotenv(".env", override=True)

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH")
FLOW_FILE_PATH = "assets/flow.json"

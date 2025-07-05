import os
import dotenv

dotenv.load_dotenv('.env', override=True)

BOT_TOKEN = os.getenv('BOT_TOKEN')
FLOW_FILE_PATH = os.getenv('NODE_FILE')
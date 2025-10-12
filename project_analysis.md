# Loyiha Tahlili Hisoboti

Sana: 2025-10-12 08:36:57

## 📁 Fayl Strukturasi

```
|   |-- 📄 .env
|   |-- 📄 .gitignore
|   |-- 📄 env.py
|   |-- 📄 nodes.json
|   |-- 📄 requirements.txt
|   |-- 📁 app/
|   |   |-- 📄 __init__.py
|   |   |-- 📄 main.py
|   |   |-- 📁 handlers/
|   |   |   |-- 📄 __init__.py
|   |   |   |-- 📄 common.py
|   |   |-- 📁 engine/
|   |   |   |-- 📄 __init__.py
|   |   |   |-- 📄 flow_controller.py
|   |   |   |-- 📄 fsm.py
|   |   |   |-- 📄 loader.py
|   |   |   |-- 📄 state_manager.py
|   |   |   |-- 📄 utils.py
|   |   |   |-- 📁 handlers/
|   |   |   |   |-- 📄 __init__.py
|   |   |   |   |-- 📄 base.py
|   |   |   |   |-- 📄 custom_handlers.py
|   |   |   |   |-- 📄 media_handlers.py
|   |   |   |   |-- 📄 message_handlers.py
|   |   |   |-- 📁 executors/
|   |   |   |   |-- 📄 __init__.py
```

## 📄 Muhim Fayllar Tarkibi

### 📄 .env

```
# @BotFather dan olingan tokeningizni shu yerga qo'ying
BOT_TOKEN="8416518955:AAEDFrJ60n9a_0OXT8thkJC0qJei3YtAHnY"

# Sxema faylining nomi
FLOW_FILE_PATH="nodes.json"

# Webhook uchun hosting manzilingiz (masalan, ngrok yoki server IP si)
# OXIRIDA / BO'LMASIN! Masalan: https://your-domain.com
BASE_WEBHOOK_URL="https://dc9ab9f43490.ngrok-free.app"
```

### 📄 .gitignore

```
# Created by https://www.toptal.com/developers/gitignore/api/python
# Edit at https://www.toptal.com/developers/gitignore?templates=python

### Python ###
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

### Python Patch ###
# Poetry local configuration file - https://python-poetry.org/docs/configuration/#local-configuration
poetry.toml

# ruff
.ruff_cache/

# LSP config files
pyrightconfig.json

# End of https://www.toptal.com/developers/gitignore/api/python
```

### 📄 env.py

```py
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
```

### 📄 nodes.json

```json
{
  "edges": [
    {
      "id": "edge_1",
      "source": "node_start_trigger",
      "target": "node_show_reply_keyboard"
    },
    {
      "id": "edge_2",
      "source": "node_profile_trigger",
      "target": "node_profile_action"
    },
    {
      "id": "edge_3",
      "source": "node_close_trigger",
      "target": "node_close_action"
    }
  ],
  "nodes": [
    {
      "id": "node_start_trigger",
      "data": {
        "filter": "command",
        "context": {
          "value": "/start"
        }
      },
      "type": "MessageTriggerNode"
    },
    {
      "id": "node_show_reply_keyboard",
      "data": {
        "buttons": [
          [
            {
              "id": "btn_reply_1",
              "text": "Mening profilim",
              "type": "reply"
            },
            {
              "id": "btn_reply_2",
              "text": " Sozlamalar",
              "type": "reply"
            }
          ],
          [
            {
              "id": "btn_reply_close",
              "text": "/close keyboard",
              "type": "reply"
            }
          ]
        ],
        "messageText": "Salom brat"
      },
      "type": "SendTextMessageNode"
    },
    {
      "id": "node_profile_trigger",
      "data": {
        "filter": "equals",
        "context": {
          "value": "Mening profilim"
        }
      },
      "type": "MessageTriggerNode"
    },
    {
      "id": "node_profile_action",
      "data": {
        "messageText": "Bu sizning profilingiz haqidagi ma'lumotlar..."
      },
      "type": "SendTextMessageNode"
    },
    {
      "id": "node_close_trigger",
      "data": {
        "filter": "equals",
        "context": {
          "value": "/close keyboard"
        }
      },
      "type": "MessageTriggerNode"
    },
    {
      "id": "node_close_action",
      "data": {
        "buttons": [],
        "messageText": " Klaviatura yopildi."
      },
      "type": "SendTextMessageNode"
    }
  ]
}

```

### 📄 requirements.txt

```
aiogram==3.1.1
fastapi==0.104.1
uvicorn==0.24.0.post1
python-dotenv==1.0.0
geopy==2.4.0
```

### 📄 app/__init__.py

```py

```

### 📄 app/main.py

```py
# app/main.py
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

from env import BASE_WEBHOOK_URL, BOT_TOKEN, FLOW_FILE_PATH
from app.engine.flow_controller import FlowController
from app.handlers.common import router as common_router

# --- Webhook Sozlamalari ---
WEBHOOK_PATH = f"/bot/{BOT_TOKEN}"
WEBHOOK_URL = f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}"

print(f"🔍 ~  ~ app/main.py:16 ~ {WEBHOOK_URL}:");

# ----------------------------

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    default_properties = DefaultBotProperties(parse_mode="HTML")
    bot = Bot(token=BOT_TOKEN, default=default_properties)
    controller = FlowController(bot=bot, schema_path=FLOW_FILE_PATH)
    dp = Dispatcher(storage=MemoryStorage(), controller=controller)
    dp.include_router(common_router)
    app.state.bot = bot
    app.state.dispatcher = dp
    await bot.set_webhook(url=WEBHOOK_URL)
    logging.info(f"Webhook o'rnatildi: {WEBHOOK_URL}")
    yield
    logging.info("Webhook o'chirilmoqda...")
    await bot.delete_webhook()
    await bot.session.close()


# ---- MUHIM QATOR ----
# Uvicorn aynan shu "app" nomli o'zgaruvchini qidiradi
app = FastAPI(lifespan=lifespan)
# --------------------


@app.get("/")
async def welcome():
    return {"message": "Welcome to the Bot API!"}


@app.post(WEBHOOK_PATH)
async def bot_webhook(request: Request):
    dispatcher: Dispatcher = request.app.state.dispatcher
    bot: Bot = request.app.state.bot
    update = types.Update(**(await request.json()))
    await dispatcher.feed_update(bot=bot, update=update)
    return {"status": "ok"}
```

### 📄 app/handlers/__init__.py

```py

```

### 📄 app/handlers/common.py

```py
# app/handlers/common.py
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from app.engine.flow_controller import FlowController
from app.engine.fsm import FlowState

router = Router()

@router.message(F.content_type.ANY, StateFilter(FlowState.waiting_for_trigger))
@router.callback_query(StateFilter(FlowState.waiting_for_trigger))
async def waiting_handler(update: Message | CallbackQuery, controller: FlowController, state: FSMContext):
    await controller.handle_update(update, state)

@router.message(F.content_type.ANY, StateFilter(None))
@router.callback_query(StateFilter(None))
async def initial_handler(update: Message | CallbackQuery, controller: FlowController, state: FSMContext):
    await controller.handle_update(update, state)
```

### 📄 app/engine/__init__.py

```py

```

### 📄 app/engine/flow_controller.py

```py
# app/engine/flow_controller.py

import logging
import re
from typing import Dict, Any

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from geopy.distance import geodesic # pip install geopy

from .fsm import FlowState
from .loader import SchemaLoader
from .executors import NodeExecutor
from .state_manager import StateManager


class FlowController:
    def __init__(self, bot: Bot, schema_path: str):
        self.bot = bot
        self.schema = SchemaLoader(schema_path)
        self.executor = NodeExecutor(bot)
        self.logger = logging.getLogger(self.__class__.__name__)

    async def handle_update(
        self, event: Message | CallbackQuery, fsm_context: FSMContext
    ):
        state_manager = StateManager(fsm_context)
        flow_context = await fsm_context.get_data()
        chat_id = event.chat.id if isinstance(event, Message) else event.message.chat.id
        
        if isinstance(event, Message):
            flow_context['message'] = event
        elif isinstance(event, CallbackQuery):
            flow_context['callback_query'] = event

        self.logger.info(f"CHAT_ID={chat_id}: Event qabul qilindi.")

        # --- YANGI MANTIQ: Triggerlarni tekshirish tartibi o'zgardi ---

        # 1-NAVBAT: Global triggerlarni tekshiramiz
        for trigger_node in self.schema.global_triggers:
            if self._check_trigger(trigger_node, event):
                self.logger.info(f"CHAT_ID={chat_id}: GLOBAL trigger ishga tushdi ({trigger_node['id']}). Joriy holat bekor qilinmoqda.")
                await fsm_context.clear()  # Joriy state'ni bekor qilamiz
                await self._traverse(trigger_node, chat_id, fsm_context, flow_context)
                return

        # Agar global trigger topilmasa, holatga asoslangan mantiqni davom ettiramiz
        current_state = await fsm_context.get_state()
        self.logger.info(f"CHAT_ID={chat_id}: Joriy holat: {current_state}")

        # 2-NAVBAT: Kutish holatidagi triggerlarni tekshiramiz
        if current_state == FlowState.waiting_for_trigger:
            paused_node_id = await state_manager.get_paused_node_id()
            if not paused_node_id:
                await state_manager.clear_state()
                return

            possible_next_nodes = self.schema.get_next_nodes(paused_node_id)
            for trigger_node in possible_next_nodes:
                if "Trigger" in trigger_node.get("type", "") and self._check_trigger(trigger_node, event):
                    self.logger.info(f"CHAT_ID={chat_id}: Kutilgan trigger ({trigger_node['id']}) ishga tushdi.")
                    await self._traverse(trigger_node, chat_id, fsm_context, flow_context, return_to_node_id=paused_node_id)
                    return
            self.logger.debug(f"CHAT_ID={chat_id}: Event kutilgan triggerlarga mos kelmadi.")
            return

        # 3-NAVBAT: Root (boshlang'ich) triggerlarni tekshiramiz (agar holat bo'sh bo'lsa)
        for trigger_node in self.schema.root_triggers:
            if self._check_trigger(trigger_node, event):
                self.logger.info(f"CHAT_ID={chat_id}: Yangi ssenariy boshlandi (Root Trigger: {trigger_node['id']})")
                await self._traverse(trigger_node, chat_id, fsm_context, flow_context)
                return
    
    # Qolgan metodlar (_traverse, _check_trigger, _check_radius) o'zgarishsiz qoladi.
    # Ularni oldingi javobdagi kabi qoldirishingiz mumkin. Quyida ularning to'liq kodi keltirilgan.

    async def _traverse(self, start_node: dict, chat_id: int, fsm_context: FSMContext, flow_context: dict, return_to_node_id: str | None = None):
        state_manager = StateManager(fsm_context)
        nodes_to_process = [start_node]
        last_processed_node_id = start_node["id"]
        while nodes_to_process:
            current_node = nodes_to_process.pop(0)
            node_type = current_node.get("type", "")
            if "Node" in node_type and "Trigger" not in node_type:
                await self.executor.execute(current_node, chat_id, flow_context)
                last_processed_node_id = current_node["id"]
            next_nodes = self.schema.get_next_nodes(current_node["id"])
            if not next_nodes: continue
            if all("Trigger" in n.get("type", "") for n in next_nodes):
                self.logger.info(f"CHAT_ID={chat_id}: Harakat bajarildi ({last_processed_node_id}), trigger(lar)ni kutish uchun pauza.")
                await state_manager.set_pause_after_node(last_processed_node_id, flow_context)
                return
            nodes_to_process.extend(next_nodes)
        if return_to_node_id:
            self.logger.info(f"CHAT_ID={chat_id}: Harakatlar shoxi tugadi. Avvalgi kutish holatiga qaytilmoqda (Node ID: {return_to_node_id}).")
            await state_manager.set_pause_after_node(return_to_node_id, flow_context)
        else:
            self.logger.info(f"CHAT_ID={chat_id}: Ssenariy shoxi tugadi. Holat tozalanmoqda.")
            await state_manager.clear_state()

    def _check_radius(self, event_location, radius_context: Dict[str, Any]) -> bool:
        try:
            center_lat, center_lng, radius_km = float(radius_context.get("lat")), float(radius_context.get("lng")), float(radius_context.get("km"))
            user_location, center_point = (event_location.latitude, event_location.longitude), (center_lat, center_lng)
            distance = geodesic(user_location, center_point).kilometers
            return distance <= radius_km
        except (ValueError, TypeError, AttributeError): return False

    def _check_trigger(self, trigger_node: dict, event: Message | CallbackQuery) -> bool:
        node_type, data = trigger_node.get("type"), trigger_node.get("data", {})
        if node_type == "CommandTriggerNode" and isinstance(event, Message):
            command = data.get("command")
            return command and event.text and event.text.startswith(command)
        if node_type == "MessageTriggerNode" and isinstance(event, Message):
            expected_type = data.get("type")
            if expected_type and expected_type != "any" and expected_type != event.content_type: return False
            filt, context = data.get("filter"), data.get("context", {})
            if not filt or filt == "any": return True
            if filt in ["equals", "contains", "starts_with", "regex", "command"] and event.text:
                value = context.get("value")
                if value is None: return False
                if filt == "equals": return event.text == value
                if filt == "contains": return value in event.text
                if filt in ["starts_with", "command"]: return event.text.startswith(value)
                if filt == "regex":
                    try: return bool(re.match(value, event.text))
                    except re.error: return False
            return False
        if node_type == "ReplyButtonTriggerNode" and isinstance(event, Message):
            selected_button = data.get("selectedButton", {})
            btn_type, btn_text = selected_button.get("type"), selected_button.get("text")
            if btn_type == "reply" and event.text == btn_text: return True
            if btn_type == "request_contact" and event.contact: return True
            if btn_type == "request_location" and event.location: return True
            return False
        if node_type in ["CallbackButtonTriggerNode", "CallbackQueryTriggerNode"] and isinstance(event, CallbackQuery):
            if not event.data: return False
            if node_type == "CallbackButtonTriggerNode": return event.data in data.get("selectedCallbacks", [])
            filt, value = data.get("filter"), data.get("context", {}).get("value")
            if filt == "any": return True
            if not filt or not value: return False
            if filt == "equals": return event.data == value
            if filt == "contains": return value in event.data
            if filt == "starts_with": return event.data.startswith(value)
            if filt == "regex":
                try: return bool(re.match(value, event.data))
                except re.error: return False
            return False
        return False
```

### 📄 app/engine/fsm.py

```py
# app/engine/fsm.py
from aiogram.fsm.state import State, StatesGroup

class FlowState(StatesGroup):
    waiting_for_trigger = State()
```

### 📄 app/engine/loader.py

```py
# app/engine/loader.py
import json
import logging
from typing import Dict, List, Any

class SchemaLoader:
    def __init__(self, file_path: str):
        self.nodes: Dict[str, Dict] = {}
        self.edges: Dict[str, List[Dict]] = {}
        self.root_triggers: List[Dict] = []
        self.global_triggers: List[Dict] = []  # <-- YANGI QO'SHILDI

        self._load(file_path)

    def _load(self, file_path: str):
        try:
            with open(file_path, 'r', encoding='utf-8') as f: data = json.load(f)
            all_nodes, all_edges = data.get('nodes', []), data.get('edges', [])
            
            self.nodes = {node['id']: node for node in all_nodes}
            for edge in all_edges:
                self.edges.setdefault(edge['source'], []).append(edge)
            
            # Root trigger'larni aniqlash (kirish bog'lanishi yo'q trigger'lar)
            target_node_ids = {edge['target'] for edge in all_edges}
            self.root_triggers = [
                node for node in all_nodes
                if 'Trigger' in node.get('type', '') and node['id'] not in target_node_ids
            ]
            
            # --- YANGI KOD: Global trigger'larni aniqlash ---
            # data.global == true bo'lgan barcha trigger'larni topamiz
            self.global_triggers = [
                node for node in all_nodes
                if 'Trigger' in node.get('type', '') and node.get('data', {}).get('global') is True
            ]
            # --- YANGI KOD TUGADI ---

            logging.info(
                f"Sxema yuklandi: {len(self.nodes)} node, {len(all_edges)} edge, "
                f"{len(self.root_triggers)} root trigger, {len(self.global_triggers)} global trigger."
            )
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.critical(f"Sxema faylini yuklashda xatolik: {e}")
            raise

    def get_node(self, node_id: str) -> Dict | None: return self.nodes.get(node_id)
    
    def get_next_nodes(self, source_node_id: str) -> List[Dict]:
        return [self.get_node(edge['target']) for edge in self.edges.get(source_node_id, []) if self.get_node(edge['target'])]
```

### 📄 app/engine/state_manager.py

```py
# app/engine/state_manager.py
from aiogram.fsm.context import FSMContext
from app.engine.fsm import FlowState

class StateManager:
    def __init__(self, fsm_context: FSMContext):
        self.context = fsm_context

    async def set_pause_after_node(self, node_id: str, flow_data: dict):
        await self.context.set_state(FlowState.waiting_for_trigger)
        flow_data['paused_after_node_id'] = node_id
        await self.context.set_data(flow_data)

    async def get_paused_node_id(self) -> str | None:
        data = await self.context.get_data()
        return data.get("paused_after_node_id")

    async def clear_state(self):
        await self.context.clear()
```

### 📄 app/engine/utils.py

```py
# app/engine/utils.py
from typing import Dict, Optional, Union
from aiogram.types import (
    InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardButton, ReplyKeyboardRemove, WebAppInfo, KeyboardButtonPollType
)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

def build_keyboard(keyboard_config: Optional[Dict]) -> Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove]]:
    if not keyboard_config: return None
    active_type = keyboard_config.get('active')
    buttons_data = keyboard_config.get(active_type)
    if not buttons_data or not isinstance(buttons_data, list) or not any(row for row in buttons_data): return None
    
    try: first_button_type = buttons_data[0][0].get('type')
    except (IndexError, AttributeError): return None

    if first_button_type in ['url', 'callback', 'web_app']:
        builder = InlineKeyboardBuilder()
        for row in buttons_data:
            buttons_to_add = []
            for btn_data in row:
                btn_type, btn_text = btn_data.get('type'), btn_data.get('text')
                if not btn_text: continue
                if btn_type == 'url' and btn_data.get('value'):
                    buttons_to_add.append(InlineKeyboardButton(text=btn_text, url=btn_data['value']))
                elif btn_type == 'callback' and btn_data.get('value'):
                    buttons_to_add.append(InlineKeyboardButton(text=btn_text, callback_data=str(btn_data['value'])))
                elif btn_type == 'web_app' and btn_data.get('webApp', {}).get('url'):
                    buttons_to_add.append(InlineKeyboardButton(text=btn_text, web_app=WebAppInfo(url=btn_data['webApp']['url'])))
            if buttons_to_add: builder.row(*buttons_to_add)
        return builder.as_markup()
    
    elif first_button_type in ['reply', 'request_contact', 'request_location', 'web_app', 'request_poll']:
        builder = ReplyKeyboardBuilder()
        for row in buttons_data:
            buttons_to_add = []
            for btn_data in row:
                if not btn_data.get('text'): continue
                params = {"text": btn_data['text']}
                btn_type = btn_data.get('type')
                if btn_type == 'request_contact': params['request_contact'] = True
                elif btn_type == 'request_location': params['request_location'] = True
                elif btn_type == 'web_app' and btn_data.get('webApp', {}).get('url'):
                    params['web_app'] = WebAppInfo(url=btn_data['webApp']['url'])
                elif btn_type == 'request_poll' and btn_data.get('pollType'):
                    params['request_poll'] = KeyboardButtonPollType(type=btn_data['pollType'])
                buttons_to_add.append(KeyboardButton(**params))
            if buttons_to_add: builder.row(*buttons_to_add)
        return builder.as_markup(resize_keyboard=True, one_time_keyboard=False)
    return None
```

### 📄 app/engine/handlers/__init__.py

```py

```

### 📄 app/engine/handlers/base.py

```py
# app/engine/handlers/base.py
import logging
from abc import ABC, abstractmethod
from typing import Dict, Any, List

from aiogram import Bot
from app.engine.utils import build_keyboard

class ActionHandler(ABC):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        raise NotImplementedError

    def _prepare_common_params(self, data: Dict[str, Any]) -> Dict[str, Any]:
        params = {}
        reply_markup = build_keyboard(data.get('keyboard'))
        if reply_markup:
            params['reply_markup'] = reply_markup
        if data.get('disableNotification'):
            params['disable_notification'] = True
        if data.get('protectContent'):
            params['protect_content'] = True
        return params

    def _get_recipients(self, data: Dict[str, Any], initial_chat_id: int) -> List[int]:
        recipients_config = data.get('recipients', {})
        ids = []
        if recipients_config.get('sendToSender', True):
            ids.append(initial_chat_id)
        additional_ids_str = recipients_config.get('additionalIds', [])
        for user_id in additional_ids_str:
            try: ids.append(int(user_id))
            except (ValueError, TypeError): self.logger.warning(f"Qo'shimcha qabul qiluvchi ID'si noto'g'ri formatda: {user_id}")
        return list(set(ids))
```

### 📄 app/engine/handlers/custom_handlers.py

```py
# app/engine/handlers/custom_handlers.py
import asyncio
from typing import Dict, Any
from .base import ActionHandler

class CustomCodeHandler(ActionHandler):
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        python_code = data.get('pythonCode', '')
        if not python_code:
            self.logger.warning("CustomCodeNode'da bajarish uchun kod yo'q.")
            return

        self.logger.info(f"CustomCodeNode kodini bajarishga tayyorlanmoqda (chat_id: {chat_id})")
        
        execution_globals = {
            'bot': self.bot,
            'chat_id': chat_id,
            'context': context,
            'asyncio': asyncio,
            'message': context.get('message'), 
            'callback': context.get('callback_query'),
        }

        try:
            exec_code = f"async def __exec_code():\n"
            exec_code += "".join(f"    {line}\n" for line in python_code.splitlines())
            exec(exec_code, execution_globals)
            coro = execution_globals['__exec_code']()
            await coro
            self.logger.info(f"CustomCodeNode kodi muvaffaqiyatli bajarildi (chat_id: {chat_id})")
        except Exception as e:
            error_message = f"Custom code'ni bajarishda xatolik yuz berdi: {e}"
            self.logger.error(error_message, exc_info=True)
            await self.bot.send_message(chat_id, f"⚠️ Kod bajarishda xatolik:\n<pre>{e}</pre>")
```

### 📄 app/engine/handlers/media_handlers.py

```py
# app/engine/handlers/media_handlers.py
from typing import Dict, Any
from .base import ActionHandler

class SendPhotoHandler(ActionHandler):
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        source_type = data.get('photoSourceType', 'url')
        photo_id = data.get('photoFileId') if source_type == 'file_id' else data.get('photoUrl')
        if not photo_id: self.logger.error(f"Node data'da 'photoFileId' yoki 'photoUrl' topilmadi: {data}"); return
        params = self._prepare_common_params(data)
        if data.get('caption'): params['caption'] = data.get('caption')
        for recipient_id in self._get_recipients(data, chat_id):
            try: await self.bot.send_photo(chat_id=recipient_id, photo=photo_id, **params)
            except Exception as e: self.logger.error(f"Rasm yuborishda xatolik (chat_id: {recipient_id}): {e}")

class SendVideoHandler(ActionHandler):
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        source_type = data.get('videoSourceType', 'url')
        video_id = data.get('videoFileId') if source_type == 'file_id' else data.get('videoUrl')
        if not video_id: self.logger.error(f"Node data'da 'videoFileId' yoki 'videoUrl' topilmadi: {data}"); return
        params = self._prepare_common_params(data)
        if data.get('caption'): params['caption'] = data.get('caption')
        # ...boshqa video parametrlari...
        for recipient_id in self._get_recipients(data, chat_id):
            try: await self.bot.send_video(chat_id=recipient_id, video=video_id, **params)
            except Exception as e: self.logger.error(f"Video yuborishda xatolik (chat_id: {recipient_id}): {e}")

class SendAudioHandler(ActionHandler):
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        source_type = data.get('audioSourceType', 'url')
        audio_id = data.get('audioFileId') if source_type == 'file_id' else data.get('audioUrl')
        if not audio_id: self.logger.error(f"Node data'da 'audioFileId' yoki 'audioUrl' topilmadi: {data}"); return
        params = self._prepare_common_params(data)
        # ...boshqa audio parametrlari...
        for recipient_id in self._get_recipients(data, chat_id):
            try: await self.bot.send_audio(chat_id=recipient_id, audio=audio_id, **params)
            except Exception as e: self.logger.error(f"Audio yuborishda xatolik (chat_id: {recipient_id}): {e}")

class SendFileHandler(ActionHandler):
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        source_type = data.get('fileSourceType', 'url')
        file_id = data.get('fileId') if source_type == 'file_id' else data.get('fileUrl')
        if not file_id: self.logger.error(f"Node data'da 'fileId' yoki 'fileUrl' topilmadi: {data}"); return
        params = self._prepare_common_params(data)
        if data.get('caption'): params['caption'] = data.get('caption')
        for recipient_id in self._get_recipients(data, chat_id):
            try: await self.bot.send_document(chat_id=recipient_id, document=file_id, **params)
            except Exception as e: self.logger.error(f"Fayl yuborishda xatolik (chat_id: {recipient_id}): {e}")
```

### 📄 app/engine/handlers/message_handlers.py

```py
# app/engine/handlers/message_handlers.py
from typing import Dict, Any
from .base import ActionHandler

class SendTextHandler(ActionHandler):
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        text = data.get('messageText', '[Matn ko\'rsatilmagan]')
        params = self._prepare_common_params(data)
        if data.get('parseMode') and data['parseMode'] != 'None':
            params['parse_mode'] = data['parseMode']
        if data.get('disableWebPagePreview'):
            params['disable_web_page_preview'] = data.get('disableWebPagePreview')
        for recipient_id in self._get_recipients(data, chat_id):
            try:
                await self.bot.send_message(chat_id=recipient_id, text=text, **params)
            except Exception as e:
                self.logger.error(f"Xabar yuborishda xatolik (chat_id: {recipient_id}): {e}")
```

### 📄 app/engine/executors/__init__.py

```py
# app/engine/executors/__init__.py
import logging
from aiogram import Bot
from typing import Dict, Any, Type

from app.engine.handlers.base import ActionHandler
from app.engine.handlers.custom_handlers import CustomCodeHandler
from app.engine.handlers.media_handlers import SendAudioHandler, SendFileHandler, SendPhotoHandler, SendVideoHandler
from app.engine.handlers.message_handlers import SendTextHandler

class NodeExecutor:
    def __init__(self, bot: Bot):
        self.bot = bot
        self.logger = logging.getLogger(self.__class__.__name__)
        self._handlers: Dict[str, Type[ActionHandler]] = {
            "SendTextMessageNode": SendTextHandler,
            "SendPhotoNode": SendPhotoHandler,
            "SendVideoNode": SendVideoHandler,
            "SendAudioNode": SendAudioHandler,
            "SendFileNode": SendFileHandler,
            "CustomCodeNode": CustomCodeHandler,
        }

    async def execute(self, node: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        node_type = node.get('type')
        handler_class = self._handlers.get(node_type)
        if not handler_class:
            self.logger.warning(f"Node turi uchun bajaruvchi (handler) topilmadi: {node_type}")
            return
        try:
            handler_instance = handler_class(self.bot)
            await handler_instance.handle(node.get('data', {}), chat_id, context)
            self.logger.info(f"Node (ID: {node.get('id')}) muvaffaqiyatli bajarildi.")
        except Exception as e:
            self.logger.error(f"Node (ID: {node.get('id')}, Turi: {node_type}) bajarilishida kutilmagan xatolik: {e}", exc_info=True)
```


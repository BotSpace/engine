# Loyiha Tahlili Hisoboti

Sana: 2025-10-16 22:27:37

## 📁 Fayl Strukturasi

```
|   |-- 📄 .gitignore
|   |-- 📄 Dockerfile
|   |-- 📄 entrypoint.sh
|   |-- 📄 env.py
|   |-- 📄 nodes.json
|   |-- 📄 requirements.txt
|   |-- 📁 app/
|   |   |-- 📄 __init__.py
|   |   |-- 📄 config.py
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
|   |-- 📁 assets/
|   |   |-- 📄 flow.json
```

## 📄 Muhim Fayllar Tarkibi

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

### 📄 Dockerfile

```
FROM python:3.13-slim

WORKDIR /code


COPY . .

RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh

CMD ["sh", "./entrypoint.sh"]


```

### 📄 entrypoint.sh

```
#!/bin/bash
set -e

python3 -m app.main

exit $?


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
      "id": "reactflow__edge-node_1760253076228_4-node_1760253095741_5",
      "type": "smart-edge",
      "style": { "stroke": "#495057", "strokeWidth": 1.5 },
      "source": "node_1760253076228_4",
      "target": "node_1760253095741_5",
      "animated": false,
      "sourceHandle": null,
      "targetHandle": null
    },
    {
      "id": "reactflow__edge-node_1760253095741_5-node_1760253241263_8",
      "type": "smart-edge",
      "style": { "stroke": "#495057", "strokeWidth": 1.5 },
      "source": "node_1760253095741_5",
      "target": "node_1760253241263_8",
      "animated": false,
      "sourceHandle": null,
      "targetHandle": null
    },
    {
      "id": "reactflow__edge-node_1760253241263_8-node_1760253131823_6",
      "type": "smart-edge",
      "style": { "stroke": "#495057", "strokeWidth": 1.5 },
      "source": "node_1760253241263_8",
      "target": "node_1760253131823_6",
      "animated": false,
      "sourceHandle": null,
      "targetHandle": null
    },
    {
      "id": "reactflow__edge-node_1760253131823_6-node_1760253280089_9",
      "type": "smart-edge",
      "style": { "stroke": "#495057", "strokeWidth": 1.5 },
      "source": "node_1760253131823_6",
      "target": "node_1760253280089_9",
      "animated": false,
      "sourceHandle": null,
      "targetHandle": null
    },
    {
      "id": "reactflow__edge-node_1760253280089_9-node_1760253161920_7",
      "type": "smart-edge",
      "style": { "stroke": "#495057", "strokeWidth": 1.5 },
      "source": "node_1760253280089_9",
      "target": "node_1760253161920_7",
      "animated": false,
      "sourceHandle": null,
      "targetHandle": null
    }
  ],
  "nodes": [
    {
      "id": "node_1760253076228_4",
      "data": { "command": "/start" },
      "type": "CommandTriggerNode",
      "width": 320,
      "height": 196,
      "dragging": false,
      "position": { "x": -967.0891191708062, "y": 1539.733718299783 },
      "selected": false,
      "positionAbsolute": { "x": -967.0891191708062, "y": 1539.733718299783 }
    },
    {
      "id": "node_1760253095741_5",
      "data": {
        "keyboard": {
          "reply": [],
          "active": "inline",
          "inline": [
            [
              {
                "id": "btn-1760253117803",
                "text": "inline_button",
                "type": "callback",
                "value": "inline_button"
              }
            ]
          ]
        },
        "parseMode": "None",
        "recipients": { "sendToSender": true, "additionalIds": [] },
        "messageText": "Yangi xabar"
      },
      "type": "SendTextMessageNode",
      "width": 400,
      "height": 499,
      "dragging": false,
      "position": { "x": -1000.4092044965785, "y": 1840.751498879408 },
      "selected": false,
      "positionAbsolute": { "x": -1000.4092044965785, "y": 1840.751498879408 }
    },
    {
      "id": "node_1760253131823_6",
      "data": {
        "keyboard": {
          "reply": [
            [{ "id": "btn-1760253156983", "text": "reply", "type": "reply" }]
          ],
          "active": "reply",
          "inline": []
        },
        "parseMode": "None",
        "recipients": { "sendToSender": true, "additionalIds": [] },
        "messageText": "inline was clicked"
      },
      "type": "SendTextMessageNode",
      "width": 400,
      "height": 499,
      "dragging": false,
      "position": { "x": -992.4579436296674, "y": 2887.880940445403 },
      "selected": false,
      "positionAbsolute": { "x": -992.4579436296674, "y": 2887.880940445403 }
    },
    {
      "id": "node_1760253161920_7",
      "data": {
        "keyboard": { "reply": [], "active": "inline", "inline": [] },
        "parseMode": "None",
        "recipients": { "sendToSender": true, "additionalIds": [] },
        "messageText": "reply was clicked"
      },
      "type": "SendTextMessageNode",
      "width": 400,
      "height": 499,
      "dragging": false,
      "position": { "x": -1030.4137974107016, "y": 3818.241422432829 },
      "selected": false,
      "positionAbsolute": { "x": -1030.4137974107016, "y": 3818.241422432829 }
    },
    {
      "id": "node_1760253241263_8",
      "data": {
        "value": "",
        "filter": "equals",
        "global": true,
        "context": { "value": "inline_button", "global": true }
      },
      "type": "CallbackQueryTriggerNode",
      "width": 320,
      "height": 320,
      "dragging": false,
      "position": { "x": -984.4494448648755, "y": 2422.9288480346568 },
      "selected": false,
      "positionAbsolute": { "x": -984.4494448648755, "y": 2422.9288480346568 }
    },
    {
      "id": "node_1760253280089_9",
      "data": {
        "selectedButton": {
          "id": "btn-1760253156983",
          "text": "reply",
          "type": "reply"
        }
      },
      "type": "ReplyButtonTriggerNode",
      "width": 320,
      "height": 148,
      "dragging": false,
      "position": { "x": -981.3086619353467, "y": 3558.694818373478 },
      "selected": true,
      "positionAbsolute": { "x": -981.3086619353467, "y": 3558.694818373478 }
    }
  ]
}

```

### 📄 requirements.txt

```
aiogram
python-dotenv

```

### 📄 app/__init__.py

```py

```

### 📄 app/config.py

```py
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
if BOT_TOKEN is None:
    raise Exception("BOT_TOKEN not found from env")
FLOW_FILE_PATH = "assets/flow.json"

```

### 📄 app/main.py

```py
import asyncio
import logging
from typing import Optional

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from app.config import BOT_TOKEN, FLOW_FILE_PATH
from app.engine.flow_controller import FlowController
from app.handlers.common import router as bot_router

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


async def main() -> None:
    logging.info("Ilova ishga tushmoqda (polling rejim)...")

    bot: Optional[Bot] = None
    try:
        default_properties = DefaultBotProperties(parse_mode="HTML")
        bot = Bot(token=str(BOT_TOKEN), default=default_properties)
        controller = FlowController(bot=bot, schema_path=FLOW_FILE_PATH)

        dp = Dispatcher(storage=MemoryStorage(), controller=controller)
        dp.include_router(bot_router)

        await dp.start_polling(bot)

    except asyncio.CancelledError:
        logging.info("Polling bekor qilindi.")
        raise
    except Exception as exc:
        logging.critical(f"Kritik xato: {exc}", exc_info=True)
    finally:
        if bot is not None:
            try:
                await bot.session.close()
                logging.info("Bot sessiyasi yopildi.")
            except Exception as e:
                logging.warning(f"Bot sessiyasini yopishda xatolik: {e}", exc_info=True)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Ilova to'xtatildi (user interrupt).")

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
from typing import Any, Dict

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from geopy.distance import geodesic  # pip install geopy

from .executors import NodeExecutor
from .fsm import FlowState
from .loader import SchemaLoader
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
            flow_context["message"] = event
        elif isinstance(event, CallbackQuery):
            flow_context["callback_query"] = event

        self.logger.info(f"CHAT_ID={chat_id}: Event qabul qilindi.")

        # --- YANGI MANTIQ: Triggerlarni tekshirish tartibi o'zgardi ---

        # 1-NAVBAT: Global triggerlarni tekshiramiz
        for trigger_node in self.schema.global_triggers:
            if self._check_trigger(trigger_node, event):
                self.logger.info(
                    f"CHAT_ID={chat_id}: GLOBAL trigger ishga tushdi ({trigger_node['id']}). Joriy holat bekor qilinmoqda."
                )
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
                if "Trigger" in trigger_node.get("type", "") and self._check_trigger(
                    trigger_node, event
                ):
                    self.logger.info(
                        f"CHAT_ID={chat_id}: Kutilgan trigger ({trigger_node['id']}) ishga tushdi."
                    )
                    await self._traverse(
                        trigger_node,
                        chat_id,
                        fsm_context,
                        flow_context,
                        return_to_node_id=paused_node_id,
                    )
                    return
            self.logger.debug(
                f"CHAT_ID={chat_id}: Event kutilgan triggerlarga mos kelmadi."
            )
            return

        # 3-NAVBAT: Root (boshlang'ich) triggerlarni tekshiramiz (agar holat bo'sh bo'lsa)
        for trigger_node in self.schema.root_triggers:
            if self._check_trigger(trigger_node, event):
                self.logger.info(
                    f"CHAT_ID={chat_id}: Yangi ssenariy boshlandi (Root Trigger: {trigger_node['id']})"
                )
                await self._traverse(trigger_node, chat_id, fsm_context, flow_context)
                return

    # Qolgan metodlar (_traverse, _check_trigger, _check_radius) o'zgarishsiz qoladi.
    # Ularni oldingi javobdagi kabi qoldirishingiz mumkin. Quyida ularning to'liq kodi keltirilgan.

    async def _traverse(
        self,
        start_node: dict,
        chat_id: int,
        fsm_context: FSMContext,
        flow_context: dict,
        return_to_node_id: str | None = None,
    ):
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
            if not next_nodes:
                continue
            if all("Trigger" in n.get("type", "") for n in next_nodes):
                self.logger.info(
                    f"CHAT_ID={chat_id}: Harakat bajarildi ({last_processed_node_id}), trigger(lar)ni kutish uchun pauza."
                )
                await state_manager.set_pause_after_node(
                    last_processed_node_id, flow_context
                )
                return
            nodes_to_process.extend(next_nodes)
        if return_to_node_id:
            self.logger.info(
                f"CHAT_ID={chat_id}: Harakatlar shoxi tugadi. Avvalgi kutish holatiga qaytilmoqda (Node ID: {return_to_node_id})."
            )
            await state_manager.set_pause_after_node(return_to_node_id, flow_context)
        else:
            self.logger.info(
                f"CHAT_ID={chat_id}: Ssenariy shoxi tugadi. Holat tozalanmoqda."
            )
            await state_manager.clear_state()

    def _check_radius(self, event_location, radius_context: Dict[str, Any]) -> bool:
        try:
            center_lat, center_lng, radius_km = (
                float(radius_context.get("lat")),
                float(radius_context.get("lng")),
                float(radius_context.get("km")),
            )
            user_location, center_point = (
                event_location.latitude,
                event_location.longitude,
            ), (center_lat, center_lng)
            distance = geodesic(user_location, center_point).kilometers
            return distance <= radius_km
        except (ValueError, TypeError, AttributeError):
            return False

    def _check_trigger(
        self, trigger_node: dict, event: Message | CallbackQuery
    ) -> bool:
        node_type, data = trigger_node.get("type"), trigger_node.get("data", {})
        if node_type == "CommandTriggerNode" and isinstance(event, Message):
            command = data.get("command")
            return command and event.text and event.text.startswith(command)
        if node_type == "MessageTriggerNode" and isinstance(event, Message):
            expected_type = data.get("type")
            if (
                expected_type
                and expected_type != "any"
                and expected_type != event.content_type
            ):
                return False
            filt, context = data.get("filter"), data.get("context", {})
            if not filt or filt == "any":
                return True
            if (
                filt in ["equals", "contains", "starts_with", "regex", "command"]
                and event.text
            ):
                value = context.get("value")
                if value is None:
                    return False
                if filt == "equals":
                    return event.text == value
                if filt == "contains":
                    return value in event.text
                if filt in ["starts_with", "command"]:
                    return event.text.startswith(value)
                if filt == "regex":
                    try:
                        return bool(re.match(value, event.text))
                    except re.error:
                        return False
            return False
        if node_type == "ReplyButtonTriggerNode" and isinstance(event, Message):
            selected_button = data.get("selectedButton", {})
            btn_type, btn_text = selected_button.get("type"), selected_button.get(
                "text"
            )
            if btn_type == "reply" and event.text == btn_text:
                return True
            if btn_type == "request_contact" and event.contact:
                return True
            if btn_type == "request_location" and event.location:
                return True
            return False
        if node_type in [
            "CallbackButtonTriggerNode",
            "CallbackQueryTriggerNode",
        ] and isinstance(event, CallbackQuery):
            if not event.data:
                return False
            if node_type == "CallbackButtonTriggerNode":
                return event.data in data.get("selectedCallbacks", [])
            filt, value = data.get("filter"), data.get("context", {}).get("value")
            if filt == "any":
                return True
            if not filt or not value:
                return False
            if filt == "equals":
                return event.data == value
            if filt == "contains":
                return value in event.data
            if filt == "starts_with":
                return event.data.startswith(value)
            if filt == "regex":
                try:
                    return bool(re.match(value, event.data))
                except re.error:
                    return False
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

### 📄 assets/flow.json

```json
{
  "nodes": [
    {
      "id": "trigger_start_command",
      "type": "CommandTriggerNode",
      "position": { "x": 100, "y": 100 },
      "data": { "command": "/start" }
    },
    {
      "id": "action_welcome_message",
      "type": "SendTextMessageNode",
      "position": { "x": 100, "y": 300 },
      "data": {
        "messageText": "Assalomu alaykum! Bizning restoranimizga xush kelibsiz. Nima bilan yordam berishim mumkin?",
        "recipients": { "sendToSender": true },
        "keyboard": {
          "inline": [
            [
              { "text": "🍽 Menu", "type": "callback", "value": "show_menu" },
              { "text": "💳 To'lov", "type": "callback", "value": "payment_options" }
            ],
            [
              { "text": "❓ Yordam", "type": "callback", "value": "support" },
              { "text": "ℹ️ Ma'lumot", "type": "callback", "value": "about_us" }
            ]
          ],
          "active": "inline"
        }
      }
    },
    {
      "id": "trigger_show_menu_callback",
      "type": "CallbackQueryTriggerNode",
      "position": { "x": -200, "y": 600 },
      "data": { "filter": "equals", "context": { "value": "show_menu" } }
    },
    {
      "id": "action_send_menu",
      "type": "SendTextMessageNode",
      "position": { "x": -200, "y": 800 },
      "data": {
        "messageText": "Bizning menyu:\n\n1. Taom 1 - 50 000 so'm\n2. Taom 2 - 75 000 so'm\n3. Ichimlik 1 - 15 000 so'm\n\nQaysi biriga buyurtma bermoqchisiz?",
        "recipients": { "sendToSender": true },
        "keyboard": {
          "inline": [
            [{ "text": "🛒 Buyurtma berish", "type": "callback", "value": "place_order" }],
            [{ "text": "⬅️ Orqaga", "type": "callback", "value": "back_to_main" }]
          ],
          "active": "inline"
        }
      }
    },
    {
      "id": "trigger_payment_options_callback",
      "type": "CallbackQueryTriggerNode",
      "position": { "x": 200, "y": 600 },
      "data": { "filter": "equals", "context": { "value": "payment_options" } }
    },
    {
      "id": "action_send_payment_options",
      "type": "SendTextMessageNode",
      "position": { "x": 200, "y": 800 },
      "data": {
        "messageText": "To'lov usullari:\n\n1. Naqd pul\n2. Karta orqali (terminal)\n3. Click/Payme (tez orada)\n\nQaysi birini afzal ko'rasiz?",
        "recipients": { "sendToSender": true },
        "keyboard": {
          "inline": [
            [{ "text": "⬅️ Orqaga", "type": "callback", "value": "back_to_main" }]
          ],
          "active": "inline"
        }
      }
    },
    {
      "id": "trigger_support_callback",
      "type": "CallbackQueryTriggerNode",
      "position": { "x": 600, "y": 600 },
      "data": { "filter": "equals", "context": { "value": "support" } }
    },
    {
      "id": "action_send_support_info",
      "type": "SendTextMessageNode",
      "position": { "x": 600, "y": 800 },
      "data": {
        "messageText": "Yordam bo'limiga xush kelibsiz. Savolingizni yozing, tez orada operatorlarimiz javob berishadi.",
        "recipients": { "sendToSender": true },
        "keyboard": {
          "inline": [
            [{ "text": "📞 Operator bilan bog'lanish", "type": "callback", "value": "contact_operator" }],
            [{ "text": "⬅️ Orqaga", "type": "callback", "value": "back_to_main" }]
          ],
          "active": "inline"
        }
      }
    },
    {
      "id": "trigger_about_us_callback",
      "type": "CallbackQueryTriggerNode",
      "position": { "x": 1000, "y": 600 },
      "data": { "filter": "equals", "context": { "value": "about_us" } }
    },
    {
      "id": "action_send_about_us",
      "type": "SendTextMessageNode",
      "position": { "x": 1000, "y": 800 },
      "data": {
        "messageText": "Bizning restoranimiz 2005 yildan buyon sizning xizmatingizda! Eng mazali taomlar va yuqori darajadagi xizmatni taklif etamiz. Manzilimiz: Toshkent sh. Buyuk Ipak Yo'li k. 15. Ish vaqti: 09:00 - 23:00.",
        "recipients": { "sendToSender": true },
        "keyboard": {
          "inline": [
            [{ "text": "⬅️ Orqaga", "type": "callback", "value": "back_to_main" }]
          ],
          "active": "inline"
        }
      }
    },
    {
      "id": "trigger_back_to_main",
      "type": "CallbackQueryTriggerNode",
      "position": { "x": 400, "y": 1000 },
      "data": { "filter": "equals", "context": { "value": "back_to_main" } }
    },
    {
      "id": "trigger_place_order_callback",
      "type": "CallbackQueryTriggerNode",
      "position": { "x": -200, "y": 1000 },
      "data": { "filter": "equals", "context": { "value": "place_order" } }
    },
    {
      "id": "action_prompt_order",
      "type": "SendTextMessageNode",
      "position": { "x": -200, "y": 1200 },
      "data": {
        "messageText": "Iltimos, buyurtma bermoqchi bo'lgan taom yoki ichimlik nomini va miqdorini yozing (masalan: Taom 1 - 2ta, Ichimlik 1 - 1ta):",
        "recipients": { "sendToSender": true }
      }
    },
    {
      "id": "trigger_receive_order",
      "type": "MessageTriggerNode",
      "position": { "x": -200, "y": 1400 },
      "data": { "type": "text" }
    },
    {
      "id": "action_process_order",
      "type": "CustomCodeNode",
      "position": { "x": -200, "y": 1600 },
      "data": {
        "pythonCode": "order_text = message.text\\n# Buyurtmani qayta ishlash logikasi bu yerda bo\\'ladi\\n# Masalan, buyurtmani bazaga saqlash yoki operatorga yuborish\\nawait message.answer(f\\\"Buyurtmangiz qabul qilindi: '{order_text}'. Tez orada siz bilan bog'lanamiz.\\\")"
      }
    },
    {
      "id": "trigger_contact_operator_callback",
      "type": "CallbackQueryTriggerNode",
      "position": { "x": 600, "y": 1000 },
      "data": { "filter": "equals", "context": { "value": "contact_operator" } }
    },
    {
      "id": "action_contact_operator",
      "type": "SendTextMessageNode",
      "position": { "x": 600, "y": 1200 },
      "data": {
        "messageText": "Operatorimiz tez orada siz bilan bog'lanadi. Iltimos kuting.",
        "recipients": { "sendToSender": true }
      }
    }
  ],
  "edges": [
    { "source": "trigger_start_command", "target": "action_welcome_message", "id": "edge_1", "type": "smart-edge" },
    { "source": "action_welcome_message", "target": "trigger_show_menu_callback", "id": "edge_2", "type": "smart-edge" },
    { "source": "action_welcome_message", "target": "trigger_payment_options_callback", "id": "edge_3", "type": "smart-edge" },
    { "source": "action_welcome_message", "target": "trigger_support_callback", "id": "edge_4", "type": "smart-edge" },
    { "source": "action_welcome_message", "target": "trigger_about_us_callback", "id": "edge_5", "type": "smart-edge" },

    { "source": "trigger_show_menu_callback", "target": "action_send_menu", "id": "edge_6", "type": "smart-edge" },
    { "source": "trigger_payment_options_callback", "target": "action_send_payment_options", "id": "edge_7", "type": "smart-edge" },
    { "source": "trigger_support_callback", "target": "action_send_support_info", "id": "edge_8", "type": "smart-edge" },
    { "source": "trigger_about_us_callback", "target": "action_send_about_us", "id": "edge_9", "type": "smart-edge" },

    { "source": "action_send_menu", "target": "trigger_back_to_main", "id": "edge_10", "type": "smart-edge" },
    { "source": "action_send_payment_options", "target": "trigger_back_to_main", "id": "edge_11", "type": "smart-edge" },
    { "source": "action_send_support_info", "target": "trigger_back_to_main", "id": "edge_12", "type": "smart-edge" },
    { "source": "action_send_about_us", "target": "trigger_back_to_main", "id": "edge_13", "type": "smart-edge" },

    { "source": "action_send_menu", "target": "trigger_place_order_callback", "id": "edge_14", "type": "smart-edge" },
    { "source": "trigger_place_order_callback", "target": "action_prompt_order", "id": "edge_15", "type": "smart-edge" },
    { "source": "action_prompt_order", "target": "trigger_receive_order", "id": "edge_16", "type": "smart-edge" },
    { "source": "trigger_receive_order", "target": "action_process_order", "id": "edge_17", "type": "smart-edge" },

    { "source": "trigger_back_to_main", "target": "action_welcome_message", "id": "edge_18", "type": "smart-edge" },

    { "source": "action_send_support_info", "target": "trigger_contact_operator_callback", "id": "edge_19", "type": "smart-edge" },
    { "source": "trigger_contact_operator_callback", "target": "action_contact_operator", "id": "edge_20", "type": "smart-edge" }
  ]
}
```


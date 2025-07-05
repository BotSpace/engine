# Loyiha Tahlili Hisoboti

Sana: 2025-07-06 02:48:44

## 📁 Fayl Strukturasi

```
... Fayl strukturasi bu yerda bo'ladi ...
```

## 📄 Muhim Fayllar Tarkibi

### 📄 .env

```
BOT_TOKEN = "8058205725:AAHiWbWdDl5jnwj_Eqz3NWY8m2itKATkkc8"
FLOW_FILE_PATH = "nodes.json"
```

### 📄 .gitignore

```
# Created by https://www.toptal.com/developers/gitignore/api/python,flask
# Edit at https://www.toptal.com/developers/gitignore?templates=python,flask

### Flask ###
instance/*
!instance/.gitignore
.webassets-cache
.env

### Flask.Python Stack ###
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

### Python ###
# Byte-compiled / optimized / DLL files

# C extensions

# Distribution / packaging

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.

# Installer logs

# Unit test / coverage reports

# Translations

# Django stuff:

# Flask stuff:

# Scrapy stuff:

# Sphinx documentation

# PyBuilder

# Jupyter Notebook

# IPython

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm

# Celery stuff

# SageMath parsed files

# Environments

# Spyder project settings

# Rope project settings

# mkdocs documentation

# mypy

# Pyre type checker

# pytype static type analyzer

# Cython debug symbols

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.

### Python Patch ###
# Poetry local configuration file - https://python-poetry.org/docs/configuration/#local-configuration
poetry.toml

# ruff
.ruff_cache/

# LSP config files
pyrightconfig.json

# End of https://www.toptal.com/developers/gitignore/api/python,flask
```

### 📄 README.md

```md
# engine
```

### 📄 app/**init**.py

```py

```

### 📄 app/engine/**init**.py

```py

```

### 📄 app/engine/executors/**init**.py

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
    """
    Action turidagi node'larni ularning turiga qarab to'g'ri "handler"ga yuboruvchi dispetcher.
    Bu klassni yangi action'lar qo'shish uchun o'zgartirish shart emas (Open/Closed Principle).
    Faqatgina _handlers lug'atiga yangi yozuv qo'shiladi.
    """
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

    async def execute(self, node: Dict[str, Any], chat_id: int):
        node_type = node.get('type')
        handler_class = self._handlers.get(node_type)

        if not handler_class:
            self.logger.warning(f"Node turi uchun bajaruvchi (handler) topilmadi: {node_type}")
            return

        try:
            handler_instance = handler_class(self.bot)
            await handler_instance.handle(node.get('data', {}), chat_id)
        except Exception as e:
            self.logger.error(
                f"Node (ID: {node.get('id')}, Turi: {node_type}) bajarilishida kutilmagan xatolik: {e}",
                exc_info=True
            )

```

### 📄 app/engine/flow_controller.py

```py
# app/engine/flow_controller.py

import logging
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, Update

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

    async def handle_update(self, event: Message | CallbackQuery, fsm_context: FSMContext):
        state_manager = StateManager(fsm_context)
        current_state = await fsm_context.get_state()

        # --- XATO TUZATILGAN QISM ---
        # Ob'ekt tipini `isinstance` yordamida tekshiramiz
        chat_id = None
        if isinstance(event, Message):
            chat_id = event.chat.id
        elif isinstance(event, CallbackQuery):
            chat_id = event.message.chat.id

        if chat_id is None:
            self.logger.warning(f"Update turidan chat_id aniqlanmadi: {type(event)}")
            return
        # --- TUZATISH TUGADI ---

        self.logger.info(f"CHAT_ID={chat_id}: Yangi event qabul qilindi. Holat: {current_state}")

        if current_state == FlowState.waiting_for_trigger:
            node_id_to_check = await state_manager.get_waiting_node_id()
            trigger_node = self.schema.get_node(node_id_to_check)

            if trigger_node and self._check_trigger(trigger_node, event):
                self.logger.info(f"CHAT_ID={chat_id}: Kutilgan trigger ({node_id_to_check}) ishga tushdi.")
                await fsm_context.clear()
                await self._traverse(trigger_node, chat_id, fsm_context)
            else:
                self.logger.debug(f"CHAT_ID={chat_id}: Event kutilgan triggerga ({node_id_to_check}) mos kelmadi.")
        else:
            for trigger_node in self.schema.root_triggers:
                if self._check_trigger(trigger_node, event):
                    self.logger.info(f"CHAT_ID={chat_id}: Yangi ssenariy boshlandi (Root Trigger: {trigger_node['id']})")
                    await self._traverse(trigger_node, chat_id, fsm_context)
                    return

    async def _traverse(self, trigger_node: dict, chat_id: int, fsm_context: FSMContext):
        state_manager = StateManager(fsm_context)
        # Boshlang'ich nuqta - triggerdan keyingi node'lar
        nodes_to_process = self.schema.get_next_nodes(trigger_node['id'])

        while nodes_to_process:
            node = nodes_to_process.pop(0)
            node_type = node.get('type', '')

            if 'Trigger' in node_type:
                self.logger.info(f"CHAT_ID={chat_id}: To'xtab, triggerni kutmoqdamiz (ID: {node['id']})")
                await state_manager.set_wait_for_trigger(node['id'])
                return

            elif 'Node' in node_type:
                await self.executor.execute(node, chat_id)
                nodes_to_process.extend(self.schema.get_next_nodes(node['id']))

        self.logger.info(f"CHAT_ID={chat_id}: Ssenariy shoxi tugadi. Holat tozalanmoqda.")
        await state_manager.clear_state()


    def _check_trigger(self, trigger_node: dict, event: Message | CallbackQuery) -> bool:
        data, node_type = trigger_node.get('data', {}), trigger_node.get('type')

        # --- 1-holat: MessageTriggerNode (matn, kontakt, lokatsiya va hk uchun) ---
        if node_type == 'MessageTriggerNode' and isinstance(event, Message):
            # Trigger qanday kontent turini kutayotganini aniqlaymiz
            expected_content_type = data.get('type') # 'text', 'contact', 'location'

            # 1a: Matn kutilganda (buyruq yoki oddiy matn)
            if expected_content_type == 'text' and event.text:
                filter_type = data.get('filter') # 'command', 'any'
                if filter_type == 'command':
                    expected_command = data.get('context', {}).get('value')
                    return event.text == expected_command
                elif filter_type == 'any':
                    return True # Har qanday matn kelsa, True

            # 1b: Kontakt kutilganda
            elif expected_content_type == 'contact' and event.contact:
                return True # Har qanday kontakt kelsa, True

            # 1c: Lokatsiya kutilganda
            elif expected_content_type == 'location' and event.location:
                return True # Har qanday lokatsiya kelsa, True

        # --- 2-holat: ReplyButtonTriggerNode (FAQAT matnli tugmalar uchun) ---
        elif node_type == 'ReplyButtonTriggerNode' and isinstance(event, Message) and event.text:
            # Trigger qaysi matn(lar)ni kutayotganini aniqlaymiz
            expected_buttons = data.get('selectedButtons', [])
            # Kelgan matn kutilayotgan matnlar ro'yxatida bo'lsa, True
            return event.text in expected_buttons

        # --- 3-holat: CallbackQueryTriggerNode (inline tugmalar uchun) ---
        # Kelajakda to'ldiriladi
        elif node_type in ['CallbackButtonTriggerNode', 'CallbackQueryTriggerNode'] and isinstance(event, CallbackQuery):
            # Bu yerda `event.data` ni tekshirish logikasi bo'ladi
            pass

        # Agar hech qaysi shart bajarilmasa
        return False

```

### 📄 app/engine/fsm.py

```py
from aiogram.fsm.state import State, StatesGroup

class FlowState(StatesGroup):
    waiting_for_trigger = State()
```

### 📄 app/engine/handlers/**init**.py

```py

```

### 📄 app/engine/handlers/base.py

```py
import logging
from abc import ABC, abstractmethod
from typing import Dict, Any, Union, Optional

from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove

# Bu funksiya sizning utils.py faylingizda deb hisoblaymiz
from app.engine.utils import build_keyboard

class ActionHandler(ABC):
    """
    Barcha Action Node handler'lari uchun abstrakt baza klassi (interfeys).
    Har bir handler shu klassdan meros oladi va o'zining `handle` metodini implementatsiya qiladi.
    Bu Liskov Substitution Principle (SOLID'ning 'L' harfi) uchun muhim.
    """
    def __init__(self, bot: Bot):
        self.bot = bot
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    async def handle(self, data: Dict[str, Any], chat_id: int):
        """
        Har bir handler ushbu metodni o'ziga xos tarzda implementatsiya qilishi SHART.
        :param data: Node'ning `data` maydonidagi ma'lumotlar.
        :param chat_id: Xabar yuboriladigan chat ID.
        """
        raise NotImplementedError

    def _prepare_common_params(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ko'pchilik `send_*` metodlari uchun umumiy bo'lgan parametrlarni tayyorlaydi.
        Bu kod takrorlanishining oldini oladi (DRY tamoyili).
        """
        buttons: Optional[list[list[dict]]] = data.get('buttons')

        # `build_keyboard` funksiyasi ReplyKeyboardRemove qaytarishi mumkin,
        # shuning uchun reply_markup None bo'lmasligi kerak
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove]] = build_keyboard(buttons)

        params = {}
        if reply_markup is not None:
            params['reply_markup'] = reply_markup

        if data.get('disableNotification'):
            params['disable_notification'] = True

        if data.get('protectContent'):
            params['protect_content'] = True

        return params
```

### 📄 app/engine/handlers/custom_handlers.py

```py
# app/engine/executors/custom_handlers.py
from typing import Dict, Any
from .base import ActionHandler

class CustomCodeHandler(ActionHandler):
    """CustomCodeNode'ni xavfsiz tarzda bajarish uchun mas'ul."""

    async def handle(self, data: Dict[str, Any], chat_id: int):
        python_code = data.get('pythonCode', '')
        if not python_code:
            self.logger.warning("CustomCodeNode'da bajarish uchun kod yo'q.")
            return

        self.logger.info(f"CustomCodeNode'ning kodini bajarishga harakat qilinmoqda (chat_id: {chat_id})")

        # DIQQAT: `exec()` funksiyasini to'g'ridan-to'g'ri ishlatish O'TA XAVFLI!
        # Bu yerda maxsus xavfsiz "sandbox" (qum qutisi) muhiti yaratish kerak.
        # Buning uchun restrictedpython, Piston API kabi kutubxonalardan foydalanish mumkin.
        # Hozircha, biz bu amaliyotning xavfliligini ko'rsatish uchun faqat log yozamiz.

        self.logger.critical("XAVFSIZLIK OGOHLANTIRISHI: Custom code execution (exec) implementatsiya qilinmagan.")
        # Misol:
        # try:
        #     # Sandbox'da kodni bajarish logikasi...
        # except Exception as e:
        #     self.logger.error(f"Custom code'ni bajarishda xatolik: {e}")
```

### 📄 app/engine/handlers/media_handlers.py

```py
# app/engine/executors/media_handlers.py
from typing import Dict, Any
from .base import ActionHandler

class SendPhotoHandler(ActionHandler):
    """SendPhotoNode'ni bajarish uchun mas'ul."""

    async def handle(self, data: Dict[str, Any], chat_id: int):
        source_type = data.get('photoSourceType', 'url')
        photo_id = data.get('photoFileId' if source_type == 'file_id' else 'photoUrl')

        if not photo_id:
            self.logger.error(f"Node data'da 'photoFileId' yoki 'photoUrl' topilmadi. Ma'lumot: {data}")
            return

        params = self._prepare_common_params(data)

        caption = data.get('caption')
        if caption:
            params['caption'] = caption

        await self.bot.send_photo(
            chat_id=chat_id,
            photo=photo_id,
            **params
        )


class SendVideoHandler(ActionHandler):
    """SendVideoNode'ni bajarish uchun mas'ul."""

    async def handle(self, data: Dict[str, Any], chat_id: int):
        source_type = data.get('videoSourceType', 'url')
        video_id = data.get('videoFileId' if source_type == 'file_id' else 'videoUrl')

        if not video_id:
            self.logger.error(f"Node data'da 'videoFileId' yoki 'videoUrl' topilmadi. Ma'lumot: {data}")
            return

        params = self._prepare_common_params(data)

        # Videoga xos parametrlarni qo'shamiz
        if data.get('caption'): params['caption'] = data.get('caption')
        if data.get('width'): params['width'] = int(data['width'])
        if data.get('height'): params['height'] = int(data['height'])
        if data.get('duration'): params['duration'] = int(data['duration'])
        if data.get('supportsStreaming'): params['supports_streaming'] = True

        await self.bot.send_video(
            chat_id=chat_id,
            video=video_id,
            **params
        )

# Xuddi shu tarzda SendAudioHandler va SendFileHandler ham yoziladi...
class SendAudioHandler(ActionHandler):
    """SendAudioNode'ni bajarish uchun mas'ul."""
    async def handle(self, data: Dict[str, Any], chat_id: int):
        # ... Audio uchun logikani implementatsiya qilish ...
        pass

class SendFileHandler(ActionHandler):
    """SendFileNode'ni bajarish uchun mas'ul."""
    async def handle(self, data: Dict[str, Any], chat_id: int):
        # ... Fayl (document) uchun logikani implementatsiya qilish ...
        pass
```

### 📄 app/engine/handlers/message_handlers.py

```py
# app/engine/executors/message_handlers.py
from typing import Dict, Any
from .base import ActionHandler

class SendTextHandler(ActionHandler):
    """SendTextMessageNode'ni bajarish uchun mas'ul."""

    async def handle(self, data: Dict[str, Any], chat_id: int):
        text = data.get('messageText', '[Matn ko\'rsatilmagan]')

        params = self._prepare_common_params(data)

        # Qo'shimcha, faqat shu node'ga xos parametrlar
        if 'parseMode' in data and data['parseMode'] != 'None':
            params['parse_mode'] = data['parseMode']

        if 'disableWebPagePreview' in data:
            params['disable_web_page_preview'] = data['disableWebPagePreview']

        await self.bot.send_message(
            chat_id=chat_id,
            text=text,
            **params
        )
```

### 📄 app/engine/loader.py

```py
import json
import logging
from typing import Dict, List, Any

class SchemaLoader:
    def __init__(self, file_path: str):
        self.nodes: Dict[str, Dict] = {}
        self.edges: Dict[str, List[Dict]] = {}
        self.root_triggers: List[Dict] = []
        self._load(file_path)

    def _load(self, file_path: str):
        try:
            with open(file_path, 'r', encoding='utf-8') as f: data = json.load(f)
            all_nodes, all_edges = data.get('nodes', []), data.get('edges', [])
            self.nodes = {node['id']: node for node in all_nodes}
            for edge in all_edges:
                self.edges.setdefault(edge['source'], []).append(edge)

            target_node_ids = {edge['target'] for edge in all_edges}
            self.root_triggers = [
                node for node in all_nodes
                if 'Trigger' in node.get('type', '') and node['id'] not in target_node_ids
            ]
            logging.info(f"Sxema yuklandi: {len(self.nodes)} node, {len(all_edges)} edge, {len(self.root_triggers)} root trigger.")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.critical(f"Sxema faylini yuklashda xatolik: {e}")
            raise

    def get_node(self, node_id: str) -> Dict | None: return self.nodes.get(node_id)
    def get_next_nodes(self, source_node_id: str) -> List[Dict]:
        return [self.get_node(edge['target']) for edge in self.edges.get(source_node_id, []) if self.get_node(edge['target'])]
```

### 📄 app/engine/node_executor.py

```py
# app/engine/node_executor.py
import logging
from aiogram import Bot
from typing import Dict, Any
from app.engine.utils import build_keyboard

class NodeExecutor:
    """Berilgan node'ning amalini bajarish uchun mas'ul."""

    def __init__(self, bot: Bot):
        self.bot = bot
        # Har bir Action node turi uchun alohida metod
        self._handlers = {
            "SendTextMessageNode": self._execute_send_text,
            "SendPhotoNode": self._execute_send_photo,
            # ... boshqa action turlari uchun metodlar ...
        }

    async def execute(self, node: Dict, chat_id: int):
        node_type = node.get('type')
        handler = self._handlers.get(node_type)
        if handler:
            logging.info(f"CHAT_ID={chat_id}: Bajarilmoqda -> {node_type} (ID: {node['id']})")
            await handler(node.get('data', {}), chat_id)
        else:
            logging.warning(f"CHAT_ID={chat_id}: {node_type} uchun bajaruvchi topilmadi. O'tkazib yuborildi.")

    # --- Action Handler Metodlari ---

    async def _execute_send_text(self, data: Dict[str, Any], chat_id: int):
        text = data.get('messageText', '[Matn topilmadi]')
        buttons = data.get('buttons')
        # Bu yerda `disable_web_page_preview`, `parse_mode` kabilarni ham
        # `data` dan olib, `send_message`ga uzatish mumkin.
        await self.bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=build_keyboard(buttons)
        )

    async def _execute_send_photo(self, data: Dict[str, Any], chat_id: int):
        # photoSourceType ga qarab file_id yoki url ishlatiladi.
        photo_id = data.get('photoFileId') or data.get('photoUrl')
        if not photo_id:
            logging.error("SendPhotoNode uchun photoFileId yoki photoUrl topilmadi.")
            return

        caption = data.get('caption', '')
        buttons = data.get('buttons')
        await self.bot.send_photo(
            chat_id=chat_id,
            photo=photo_id,
            caption=caption,
            reply_markup=build_keyboard(buttons)
        )
```

### 📄 app/engine/state_manager.py

```py
from aiogram.fsm.context import FSMContext
from app.engine.fsm import FlowState

class StateManager:
    def __init__(self, fsm_context: FSMContext):
        self.context = fsm_context

    async def set_wait_for_trigger(self, node_id: str):
        await self.context.set_state(FlowState.waiting_for_trigger)
        await self.context.update_data(waiting_for_node_id=node_id)

    async def get_waiting_node_id(self) -> str | None:
        data = await self.context.get_data()
        return data.get("waiting_for_node_id")

    async def clear_state(self):
        await self.context.clear()
```

### 📄 app/engine/utils.py

```py
from typing import List, Dict, Optional, Union
from aiogram.types import (
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    ReplyKeyboardRemove
)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

def build_keyboard(buttons_data: Optional[List[List[Dict]]]) -> Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove]]:
    if buttons_data is None: return None
    if not buttons_data: return ReplyKeyboardRemove()
    if not any(row for row in buttons_data): return None

    try:
        first_button_type = buttons_data[0][0].get('type')
    except (IndexError, AttributeError):
        return None

    if first_button_type in ['url', 'callback']:
        builder = InlineKeyboardBuilder()
        for row in buttons_data:
            buttons = [
                InlineKeyboardButton(text=btn['text'], url=btn.get('value')) if btn['type'] == 'url'
                else InlineKeyboardButton(text=btn['text'], callback_data=str(btn.get('value')))
                for btn in row if btn.get('text') and btn.get('value')
            ]
            if buttons: builder.row(*buttons)
        return builder.as_markup()

    elif first_button_type in ['reply', 'request_contact', 'request_location']:
        builder = ReplyKeyboardBuilder()
        for row in buttons_data:
            buttons = []
            for btn in row:
                if not btn.get('text'): continue
                request_contact = btn['type'] == 'request_contact'
                request_location = btn['type'] == 'request_location'
                buttons.append(KeyboardButton(
                    text=btn['text'],
                    request_contact=request_contact,
                    request_location=request_location
                ))
            if buttons: builder.row(*buttons)
        return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

    return None
```

### 📄 app/handlers/**init**.py

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

# Bu handler foydalanuvchi FlowState.waiting_for_trigger holatida bo'lganda ishlaydi.
# state=... o'rniga StateFilter(...) ishlatiladi.
@router.message(F.content_type.ANY, StateFilter(FlowState.waiting_for_trigger))
@router.callback_query(StateFilter(FlowState.waiting_for_trigger))
async def waiting_handler(update: Message | CallbackQuery, controller: FlowController, state: FSMContext):
    await controller.handle_update(update, state)

# Bu handler foydalanuvchi holati bo'sh (None) bo'lganda ishlaydi.
@router.message(F.content_type.ANY, StateFilter(None))
@router.callback_query(StateFilter(None))
async def initial_handler(update: Message | CallbackQuery, controller: FlowController, state: FSMContext):
    await controller.handle_update(update, state)
```

### 📄 app/main.py

```py
# app/main.py (YANGILANGAN VERSIYA)

import logging
import requests
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties # <--- QO'SHILDI: import

from env import BOT_TOKEN, FLOW_FILE_PATH
from app.engine.flow_controller import FlowController
from app.handlers.common import router as common_router

# --- Webhook Sozlamalari (5-qadamda to'ldiriladi) ---
BASE_WEBHOOK_URL = "https://6ded-84-54-120-94.ngrok-free.app"
WEBHOOK_PATH = f"/bot/{BOT_TOKEN}"
WEBHOOK_URL = f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}"
# ----------------------------

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- O'ZGARISH SHU YERDA ---
    # Botning standart xususiyatlarini belgilaymiz
    default_properties = DefaultBotProperties(parse_mode="HTML")
    bot = Bot(token=BOT_TOKEN, default=default_properties)
    # --- O'ZGARISH TUGADI ---

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

app = FastAPI(lifespan=lifespan)

@app.post(WEBHOOK_PATH)
async def bot_webhook(request: Request):
    dispatcher: Dispatcher = request.app.state.dispatcher
    bot: Bot = request.app.state.bot

    update = types.Update(**(await request.json()))
    await dispatcher.feed_update(bot=bot, update=update)
    return {'status': 'ok'}
```

### 📄 env.py

```py
# env.py
import os
from dotenv import load_dotenv

load_dotenv('.env')

BOT_TOKEN = os.getenv("BOT_TOKEN")
FLOW_FILE_PATH = os.getenv("FLOW_FILE_PATH")

print(" LOG_ID: [0d1a24dae806] ~ 🚀 ~ file: env.py:8 ~  BOT_TOKEN:",BOT_TOKEN)

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN .env faylida topilmadi yoki bo'sh!")
if not FLOW_FILE_PATH:
    raise ValueError("FLOW_FILE_PATH .env faylida topilmadi yoki bo'sh!")
```

### 📄 nodes.json

```json
{
  "nodes": [
    {
      "id": "dndnode_3",
      "type": "MessageTriggerNode",
      "position": {
        "x": 998.758500144829,
        "y": 2131.389457003139
      },
      "data": {
        "type": "text",
        "filter": "command",
        "context": {
          "value": "/start"
        },
        "messageText": "Familyangizni kiriting"
      },
      "width": 400,
      "height": 530,
      "selected": false,
      "dragging": false,
      "positionAbsolute": {
        "x": 998.758500144829,
        "y": 2131.389457003139
      }
    },
    {
      "id": "dndnode_4",
      "type": "SendTextMessageNode",
      "position": {
        "x": 1010,
        "y": 2740
      },
      "data": {
        "recipients": {
          "sendToSender": true,
          "additionalIds": []
        },
        "messageText": "Assalomu Alekum tz sotib qoch kursi botiga xush kelibsiz",
        "parseMode": "None",
        "buttons": [
          [
            {
              "id": "btn-1751742748572",
              "text": "ro'yxatdan o'tish",
              "type": "reply"
            }
          ]
        ]
      },
      "width": 400,
      "height": 257,
      "selected": false,
      "positionAbsolute": {
        "x": 1009.8796938244038,
        "y": 2742.502822902669
      },
      "dragging": false
    },
    {
      "id": "dndnode_7",
      "type": "ReplyButtonTriggerNode",
      "position": {
        "x": -131.9586988059396,
        "y": 1789.9701225187594
      },
      "data": {
        "selectedButtons": ["ro'yxatdan o'tish", "Ro'yxatdan o'tish"]
      },
      "width": 320,
      "height": 169,
      "selected": false,
      "positionAbsolute": {
        "x": -131.9586988059396,
        "y": 1789.9701225187594
      },
      "dragging": false
    },
    {
      "id": "dndnode_8",
      "type": "SendTextMessageNode",
      "position": {
        "x": -178.5446818842657,
        "y": 2068.0242645371136
      },
      "data": {
        "recipients": {
          "sendToSender": true,
          "additionalIds": []
        },
        "messageText": "Iltmos telefon raqamingizni yuboring",
        "parseMode": "None",
        "buttons": [
          [
            {
              "id": "btn-1751742833106",
              "text": "📱 Kontakt",
              "type": "request_contact"
            }
          ]
        ]
      },
      "width": 400,
      "height": 530,
      "selected": false,
      "dragging": false
    },
    {
      "id": "dndnode_9",
      "type": "MessageTriggerNode", // <--- O'ZGARTIRILDI
      "position": {
        "x": -132.5348985878946,
        "y": 2673.0858638282957
      },
      "data": {
        "type": "contact", // <--- QO'SHILDI
        "filter": "any", // <--- QO'SHILDI
        "context": {}
      },
      "width": 320,
      "height": 169,
      "selected": false,
      "positionAbsolute": {
        "x": -132.5348985878946,
        "y": 2673.0858638282957
      },
      "dragging": false
    },
    {
      "id": "dndnode_10",
      "type": "SendTextMessageNode",
      "position": {
        "x": -124.86660137183269,
        "y": 3005.1815444286262
      },
      "data": {
        "recipients": {
          "sendToSender": true,
          "additionalIds": []
        },
        "messageText": "Iltimos joylashuvingizni kiriting",
        "parseMode": "None",
        "buttons": [
          [
            {
              "id": "btn-1751742892939",
              "text": "📍 Lokatsiya",
              "type": "request_location"
            }
          ]
        ]
      },
      "width": 400,
      "height": 530,
      "selected": false,
      "dragging": false
    },
    {
      "id": "dndnode_11",
      "type": "ReplyButtonTriggerNode",
      "position": {
        "x": -89.64036079749326,
        "y": 3599.3322878980885
      },
      "data": {
        "selectedButtons": ["📍 Lokatsiya"]
      },
      "width": 320,
      "height": 169,
      "selected": false,
      "positionAbsolute": {
        "x": -89.64036079749326,
        "y": 3599.3322878980885
      },
      "dragging": false
    },
    {
      "id": "dndnode_12",
      "type": "SendTextMessageNode",
      "position": {
        "x": -128.94038402981028,
        "y": 3827.4042188972226
      },
      "data": {
        "recipients": {
          "sendToSender": true,
          "additionalIds": []
        },
        "messageText": "Uylanganmisiz",
        "parseMode": "None",
        "buttons": [
          [
            {
              "id": "btn-1751742928047",
              "text": "Ha",
              "type": "reply"
            },
            {
              "id": "btn-1751742931953",
              "text": "Yo'q",
              "type": "reply"
            }
          ]
        ]
      },
      "width": 400,
      "height": 530,
      "selected": false,
      "positionAbsolute": {
        "x": -128.94038402981028,
        "y": 3827.4042188972226
      },
      "dragging": false
    },
    {
      "id": "dndnode_13",
      "type": "ReplyButtonTriggerNode",
      "position": {
        "x": -513.2058287419962,
        "y": 4424.763473819695
      },
      "data": {
        "selectedButtons": ["Ha"]
      },
      "width": 320,
      "height": 193,
      "selected": false,
      "positionAbsolute": {
        "x": -513.2058287419962,
        "y": 4424.763473819695
      },
      "dragging": false
    },
    {
      "id": "dndnode_14",
      "type": "SendTextMessageNode",
      "position": {
        "x": -572.2941872663575,
        "y": 4803.744634422446
      },
      "data": {
        "recipients": {
          "sendToSender": true,
          "additionalIds": []
        },
        "messageText": "Bo'ydoq emasligingizdan hursandman",
        "parseMode": "None"
      },
      "width": 400,
      "height": 530,
      "selected": false,
      "dragging": false,
      "positionAbsolute": {
        "x": -572.2941872663575,
        "y": 4803.744634422446
      }
    },
    {
      "id": "dndnode_15",
      "type": "SendTextMessageNode",
      "position": {
        "x": -187.4868458599613,
        "y": 5406.399058369585
      },
      "data": {
        "recipients": {
          "sendToSender": true,
          "additionalIds": []
        },
        "messageText": "Ma'lumotlaringizni adminga jo'natdim tez orada bog'lanam",
        "parseMode": "None"
      },
      "width": 400,
      "height": 530,
      "selected": false,
      "dragging": false,
      "positionAbsolute": {
        "x": -187.4868458599613,
        "y": 5406.399058369585
      }
    },
    {
      "id": "dndnode_19",
      "type": "ReplyButtonTriggerNode",
      "position": {
        "x": 281.62243925130485,
        "y": 4419.879161017825
      },
      "data": {
        "selectedButtons": ["Yo'q"]
      },
      "width": 320,
      "height": 193,
      "selected": false,
      "positionAbsolute": {
        "x": 281.62243925130485,
        "y": 4419.879161017825
      },
      "dragging": false
    },
    {
      "id": "dndnode_21",
      "type": "SendTextMessageNode",
      "position": {
        "x": 210.32820993866676,
        "y": 4735.013105403038
      },
      "data": {
        "recipients": {
          "sendToSender": true,
          "additionalIds": []
        },
        "messageText": "Siz uchun afsusdaman tezro uylaning",
        "parseMode": "None"
      },
      "width": 400,
      "height": 530,
      "selected": false,
      "dragging": false,
      "positionAbsolute": {
        "x": 210.32820993866676,
        "y": 4735.013105403038
      }
    },
    {
      "id": "dndnode_0",
      "type": "MessageTriggerNode",
      "position": {
        "x": -157.74199782446624,
        "y": 688.3148655163712
      },
      "data": {
        "type": "text",
        "filter": "command",
        "context": {
          "value": "/start"
        }
      },
      "width": 400,
      "height": 327,
      "selected": false,
      "positionAbsolute": {
        "x": -157.74199782446624,
        "y": 688.3148655163712
      },
      "dragging": false
    },
    {
      "id": "dndnode_1",
      "type": "SendTextMessageNode",
      "position": {
        "x": -163.6358458176362,
        "y": 1111.8844250813556
      },
      "data": {
        "recipients": {
          "sendToSender": true,
          "additionalIds": []
        },
        "messageText": "Salom kazzob botga xush kelibsiz",
        "parseMode": "None",
        "buttons": [
          [
            {
              "id": "btn-1751751011182",
              "text": "Ro'yxatdan o'tish",
              "type": "reply"
            }
          ]
        ]
      },
      "width": 400,
      "height": 530,
      "selected": false,
      "dragging": false,
      "positionAbsolute": {
        "x": -163.6358458176362,
        "y": 1111.8844250813556
      }
    },
    {
      "id": "dndnode_2",
      "type": "MessageTriggerNode",
      "position": {
        "x": 996.1053977677254,
        "y": 1800.954390725774
      },
      "data": {
        "type": "text",
        "filter": "any",
        "context": {}
      },
      "width": 400,
      "height": 257,
      "selected": false,
      "positionAbsolute": {
        "x": 996.1053977677254,
        "y": 1800.954390725774
      },
      "dragging": false
    },
    {
      "id": "dndnode_3",
      "type": "SendTextMessageNode",
      "position": {
        "x": 998.758500144829,
        "y": 2131.389457003139
      },
      "data": {
        "recipients": {
          "sendToSender": true,
          "additionalIds": []
        },
        "messageText": "Familyangizni kiriting",
        "parseMode": "None"
      },
      "width": 400,
      "height": 530,
      "selected": false,
      "dragging": false,
      "positionAbsolute": {
        "x": 998.758500144829,
        "y": 2131.389457003139
      }
    },
    {
      "id": "dndnode_4",
      "type": "MessageTriggerNode",
      "position": {
        "x": 1010,
        "y": 2740
      },
      "data": {
        "type": "text",
        "filter": "any",
        "context": {}
      },
      "width": 400,
      "height": 257,
      "selected": false,
      "positionAbsolute": {
        "x": 1009.8796938244038,
        "y": 2742.502822902669
      },
      "dragging": false
    },
    {
      "id": "dndnode_5",
      "type": "SendTextMessageNode",
      "position": {
        "x": 1035.462702710271,
        "y": 3132.6810748558128
      },
      "data": {
        "recipients": {
          "sendToSender": true,
          "additionalIds": []
        },
        "messageText": "Adminga yuborildi",
        "parseMode": "None"
      },
      "width": 400,
      "height": 530,
      "selected": false,
      "dragging": false
    },
    {
      "id": "dndnode_0",
      "type": "MessageTriggerNode",
      "position": {
        "x": -157.74199782446624,
        "y": 688.3148655163712
      },
      "data": {
        "type": "text",
        "filter": "command",
        "context": {
          "value": "/start"
        }
      },
      "width": 400,
      "height": 327,
      "selected": false,
      "positionAbsolute": {
        "x": -157.74199782446624,
        "y": 688.3148655163712
      },
      "dragging": false
    },
    {
      "id": "dndnode_1",
      "type": "SendTextMessageNode",
      "position": {
        "x": -163.6358458176362,
        "y": 1111.8844250813556
      },
      "data": {
        "recipients": {
          "sendToSender": true,
          "additionalIds": []
        },
        "messageText": "Salom kazzob botga xush kelibsiz",
        "parseMode": "None",
        "buttons": [
          [
            {
              "id": "btn-1751751011182",
              "text": "Ro'yxatdan o'tish",
              "type": "reply"
            }
          ]
        ]
      },
      "width": 400,
      "height": 530,
      "selected": false,
      "positionAbsolute": {
        "x": -163.6358458176362,
        "y": 1111.8844250813556
      },
      "dragging": false
    }
  ],
  "edges": [
    {
      "source": "dndnode_3",
      "sourceHandle": "out",
      "target": "dndnode_4",
      "targetHandle": null,
      "id": "reactflow__edge-dndnode_3out-dndnode_4"
    },
    {
      "source": "dndnode_7",
      "sourceHandle": null,
      "target": "dndnode_8",
      "targetHandle": null,
      "id": "reactflow__edge-dndnode_7-dndnode_8"
    },
    {
      "source": "dndnode_8",
      "sourceHandle": null,
      "target": "dndnode_9",
      "targetHandle": null,
      "id": "reactflow__edge-dndnode_8-dndnode_9"
    },
    {
      "source": "dndnode_9",
      "sourceHandle": null,
      "target": "dndnode_10",
      "targetHandle": null,
      "id": "reactflow__edge-dndnode_9-dndnode_10"
    },
    {
      "source": "dndnode_10",
      "sourceHandle": null,
      "target": "dndnode_11",
      "targetHandle": null,
      "id": "reactflow__edge-dndnode_10-dndnode_11"
    },
    {
      "source": "dndnode_11",
      "sourceHandle": null,
      "target": "dndnode_12",
      "targetHandle": null,
      "id": "reactflow__edge-dndnode_11-dndnode_12"
    },
    {
      "source": "dndnode_12",
      "sourceHandle": null,
      "target": "dndnode_13",
      "targetHandle": null,
      "id": "reactflow__edge-dndnode_12-dndnode_13",
      "selected": false
    },
    {
      "source": "dndnode_13",
      "sourceHandle": null,
      "target": "dndnode_14",
      "targetHandle": null,
      "id": "reactflow__edge-dndnode_13-dndnode_14",
      "selected": false
    },
    {
      "source": "dndnode_14",
      "sourceHandle": null,
      "target": "dndnode_15",
      "targetHandle": null,
      "id": "reactflow__edge-dndnode_14-dndnode_15",
      "selected": false
    },
    {
      "source": "dndnode_12",
      "sourceHandle": null,
      "target": "dndnode_19",
      "targetHandle": null,
      "id": "reactflow__edge-dndnode_12-dndnode_19"
    },
    {
      "source": "dndnode_19",
      "sourceHandle": null,
      "target": "dndnode_21",
      "targetHandle": null,
      "id": "reactflow__edge-dndnode_19-dndnode_21"
    },
    {
      "source": "dndnode_21",
      "sourceHandle": null,
      "target": "dndnode_15",
      "targetHandle": null,
      "id": "reactflow__edge-dndnode_21-dndnode_15"
    },
    {
      "source": "dndnode_3",
      "sourceHandle": null,
      "target": "dndnode_4",
      "targetHandle": "in",
      "id": "reactflow__edge-dndnode_3-dndnode_4",
      "selected": false
    },
    {
      "source": "dndnode_2",
      "sourceHandle": "out",
      "target": "dndnode_3",
      "targetHandle": null,
      "id": "reactflow__edge-dndnode_2out-dndnode_3"
    },
    {
      "source": "dndnode_4",
      "sourceHandle": "out",
      "target": "dndnode_5",
      "targetHandle": null,
      "id": "reactflow__edge-dndnode_4out-dndnode_5"
    },
    {
      "source": "dndnode_0",
      "sourceHandle": "out",
      "target": "dndnode_1",
      "targetHandle": null,
      "id": "reactflow__edge-dndnode_0out-dndnode_1"
    },
    {
      "source": "dndnode_1",
      "sourceHandle": null,
      "target": "dndnode_7",
      "targetHandle": null,
      "id": "reactflow__edge-dndnode_1-dndnode_7"
    }
  ]
}
```

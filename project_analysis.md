# Loyiha Tahlili Hisoboti

Sana: 2025-07-11 01:07:46

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

### 📄 app/__init__.py

```py

```

### 📄 app/engine/__init__.py

```py

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
    """
    Action turidagi node'larni ularning turiga qarab to'g'ri "handler"ga yuboruvchi dispetcher.
    """
    def __init__(self, bot: Bot):
        self.bot = bot
        self.logger = logging.getLogger(self.__class__.__name__)
        
        # Node turi va uni bajaruvchi Handler klassi o'rtasidagi bog'liqlik
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
            # Handler'dan obyekt yaratamiz va `handle` metodini chaqiramiz
            handler_instance = handler_class(self.bot)
            await handler_instance.handle(node.get('data', {}), chat_id, context)
            self.logger.info(f"Node (ID: {node.get('id')}) muvaffaqiyatli bajarildi.")
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

    # --- YORDAMCHI FUNKSIYA (RADIUSNI TEKSHIRISH UCHUN) ---
    def _check_radius(self, event_location, radius_context: Dict[str, Any]) -> bool:
        """Berilgan nuqta belgilangan radius ichidaligini tekshiradi."""
        try:
            # Frontend'dan kelgan qiymatlarni float'ga o'giramiz
            center_lat = float(radius_context.get("lat"))
            center_lng = float(radius_context.get("lng"))
            radius_km = float(radius_context.get("km"))
            
            # Foydalanuvchi yuborgan lokatsiya
            user_location = (event_location.latitude, event_location.longitude)
            # Markaziy nuqta
            center_point = (center_lat, center_lng)
            
            # Ikki nuqta orasidagi masofani hisoblaymiz
            distance = geodesic(user_location, center_point).kilometers
            
            self.logger.debug(f"Radius tekshiruvi: Masofa {distance:.2f}km, Talab {radius_km}km.")
            return distance <= radius_km
        except (ValueError, TypeError, AttributeError):
            # Agar frontenddan kelgan qiymatlar son bo'lmasa
            self.logger.warning(f"Radius uchun noto'g'ri qiymatlar keldi: {radius_context}")
            return False

    async def handle_update(
        self, event: Message | CallbackQuery, fsm_context: FSMContext
    ):
        # Bu metod o'zgarishsiz qoladi, avvalgi javobdagi versiya to'g'ri
        state_manager = StateManager(fsm_context)
        current_state = await fsm_context.get_state()
        flow_context = await fsm_context.get_data()

        chat_id = event.chat.id if isinstance(event, Message) else event.message.chat.id
        
        if isinstance(event, Message):
            flow_context['message'] = event
        elif isinstance(event, CallbackQuery):
            flow_context['callback_query'] = event

        self.logger.info(
            f"CHAT_ID={chat_id}: Event qabul qilindi. Holat: {current_state}"
        )

        if current_state == FlowState.waiting_for_trigger:
            paused_node_id = await state_manager.get_paused_node_id()
            if not paused_node_id:
                self.logger.warning(f"CHAT_ID={chat_id}: Holat 'waiting' lekin 'paused_node_id' topilmadi. Holat tozalanmoqda.")
                await state_manager.clear_state()
                return

            possible_next_nodes = self.schema.get_next_nodes(paused_node_id)
            for trigger_node in possible_next_nodes:
                if "Trigger" in trigger_node.get("type", "") and self._check_trigger(trigger_node, event):
                    self.logger.info(f"CHAT_ID={chat_id}: Kutilgan trigger ({trigger_node['id']}) ishga tushdi.")
                    await fsm_context.clear()
                    await self._traverse(trigger_node, chat_id, fsm_context, flow_context)
                    return
            self.logger.debug(f"CHAT_ID={chat_id}: Event kutilgan triggerlarga mos kelmadi.")
        else:
            for trigger_node in self.schema.root_triggers:
                if self._check_trigger(trigger_node, event):
                    self.logger.info(f"CHAT_ID={chat_id}: Yangi ssenariy boshlandi (Root Trigger: {trigger_node['id']})")
                    await self._traverse(trigger_node, chat_id, fsm_context, flow_context)
                    return

    async def _traverse(self, start_node: dict, chat_id: int, fsm_context: FSMContext, flow_context: dict):
        # Bu metod ham o'zgarishsiz qoladi
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
                self.logger.info(f"CHAT_ID={chat_id}: Harakat bajarildi ({last_processed_node_id}), trigger(lar)ni kutish uchun pauza.")
                await state_manager.set_pause_after_node(last_processed_node_id, flow_context)
                return

            nodes_to_process.extend(next_nodes)

        self.logger.info(f"CHAT_ID={chat_id}: Ssenariy shoxi tugadi. Holat tozalanmoqda.")
        await state_manager.clear_state()

    # --- _check_trigger METODINING TO'LIQ IMPLEMENTATSIYASI ---
    def _check_trigger(self, trigger_node: dict, event: Message | CallbackQuery) -> bool:
        """Trigger shartlarini tekshiruvchi asosiy funksiya."""
        node_type = trigger_node.get("type")
        data = trigger_node.get("data", {})
        
        # --- MessageTriggerNode ---
        if node_type == "MessageTriggerNode" and isinstance(event, Message):
            expected_type = data.get("type")
            
            # 1. Kutilgan xabar turi va kelgan xabar turi mosligini tekshiramiz
            if expected_type != "any" and expected_type != event.content_type:
                return False

            # 2. Agar turlar mos kelsa, endi filterni tekshiramiz
            filt = data.get("filter")
            context = data.get("context", {})

            # Agar filter yo'q yoki "har qanday" bo'lsa, trigger ishlaydi
            if not filt or filt == "any":
                return True

            # --- Matnli filtrlar ---
            if filt in ["equals", "contains", "starts_with", "regex", "command"]:
                if not event.text: return False
                value = context.get("value")
                if value is None: return False
                
                if filt == "equals": return event.text == value
                if filt == "contains": return value in event.text
                if filt in ["starts_with", "command"]: return event.text.startswith(value)
                if filt == "regex":
                    try:
                        return bool(re.match(value, event.text))
                    except re.error:
                        self.logger.warning(f"Noto'g'ri regex pattern: {value}")
                        return False
            
            # --- Joylashuv filtri ---
            if filt == "radius":
                if not event.location or not context.get("radius"): return False
                return self._check_radius(event.location, context["radius"])

            # --- Fayl kengaytmasi filtri (faqat hujjat uchun) ---
            if filt == "extension":
                if not event.document or not event.document.file_name: return False
                value = context.get("value", "").lower().lstrip('.')
                if not value: return False
                return event.document.file_name.lower().endswith(f".{value}")

            # --- Fayl hajmi filtri ---
            if filt == "size":
                file_size_bytes = 0
                if event.photo: file_size_bytes = event.photo[-1].file_size
                elif event.video: file_size_bytes = event.video.file_size
                elif event.audio: file_size_bytes = event.audio.file_size
                elif event.document: file_size_bytes = event.document.file_size
                
                if file_size_bytes == 0: return False

                try:
                    size_context = context.get("size", {})
                    min_mb_str = size_context.get("min")
                    max_mb_str = size_context.get("max")
                    file_size_mb = file_size_bytes / (1024 * 1024)

                    # Minimal hajmni tekshirish
                    if min_mb_str and file_size_mb < float(min_mb_str):
                        return False
                    # Maksimal hajmni tekshirish
                    if max_mb_str and file_size_mb > float(max_mb_str):
                        return False
                    return True # Barcha shartlar bajarildi
                except (ValueError, TypeError):
                    self.logger.warning(f"Fayl hajmi uchun noto'g'ri qiymatlar: {context.get('size')}")
                    return False
            
            return False # Agar hech qaysi filter mos kelmasa

        # --- ReplyButtonTriggerNode ---
        elif node_type == "ReplyButtonTriggerNode" and isinstance(event, Message):
            selected_button: dict | None = data.get("selectedButton")
            if not selected_button: return False

            btn_type, btn_text = selected_button.get("type"), selected_button.get("text")
            
            if btn_type == "reply" and event.text == btn_text: return True
            if btn_type == "request_contact" and event.contact: return True
            if btn_type == "request_location" and event.location: return True
            return False

        # --- CallbackButtonTriggerNode & CallbackQueryTriggerNode ---
        elif node_type in ["CallbackButtonTriggerNode", "CallbackQueryTriggerNode"] and isinstance(event, CallbackQuery):
            if not event.data: return False
            
            if node_type == "CallbackButtonTriggerNode":
                selected_callbacks = data.get("selectedCallbacks", [])
                return event.data in selected_callbacks
            
            if node_type == "CallbackQueryTriggerNode":
                filt, value = data.get("filter"), data.get("context", {}).get("value")
                if filt == "any": return True
                if not filt or not value: return False
                
                if filt == "equals" and event.data == value: return True
                if filt == "contains" and value in event.data: return True
                if filt == "starts_with" and event.data.startswith(value): return True
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
from aiogram.fsm.state import State, StatesGroup

class FlowState(StatesGroup):
    waiting_for_trigger = State()
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
    """
    Barcha Action Node handler'lari uchun abstrakt baza klassi (interfeys).
    """
    def __init__(self, bot: Bot):
        self.bot = bot
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        """
        Har bir handler ushbu metodni o'ziga xos tarzda implementatsiya qilishi SHART.
        :param data: Node'ning `data` maydonidagi ma'lumotlar.
        :param chat_id: Xabar yuboriladigan chat ID.
        :param context: Sxema bo'ylab yuradigan umumiy ma'lumotlar lug'ati.
        """
        raise NotImplementedError

    def _prepare_common_params(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ko'pchilik `send_*` metodlari uchun umumiy bo'lgan parametrlarni tayyorlaydi.
        """
        params = {}
        
        # Yangi `build_keyboard` funksiyasiga butun konfiguratsiyani uzatamiz
        reply_markup = build_keyboard(data.get('keyboard'))
        if reply_markup:
            params['reply_markup'] = reply_markup

        if data.get('disableNotification'):
            params['disable_notification'] = True
        
        if data.get('protectContent'):
            params['protect_content'] = True
            
        return params

    def _get_recipients(self, data: Dict[str, Any], initial_chat_id: int) -> List[int]:
        """Qabul qiluvchilar ro'yxatini shakllantiradi."""
        recipients_config = data.get('recipients', {})
        ids = []
        
        if recipients_config.get('sendToSender', True):
            ids.append(initial_chat_id)
            
        additional_ids_str = recipients_config.get('additionalIds', [])
        for user_id in additional_ids_str:
            try:
                ids.append(int(user_id))
            except (ValueError, TypeError):
                self.logger.warning(f"Qo'shimcha qabul qiluvchi ID'si noto'g'ri formatda: {user_id}")
        
        # Dublikatlarni olib tashlaymiz
        return list(set(ids))
```

### 📄 app/engine/handlers/custom_handlers.py

```py
# app/engine/handlers/custom_handlers.py
import asyncio
from typing import Dict, Any
from .base import ActionHandler

class CustomCodeHandler(ActionHandler):
    """CustomCodeNode'ni xavfsiz tarzda bajarish uchun mas'ul."""

    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        python_code = data.get('pythonCode', '')
        if not python_code:
            self.logger.warning("CustomCodeNode'da bajarish uchun kod yo'q.")
            return

        self.logger.info(f"CustomCodeNode kodini bajarishga tayyorlanmoqda (chat_id: {chat_id})")
        
        # XAVFSIZLIK OGOHLANTIRISHI:
        # `exec()` yoki `eval()` funksiyalarini to'g'ridan-to'g'ri ishlatish O'TA XAVFLI!
        # Bu serverda istalgan kodni bajarish imkonini berib, jiddiy xavfsizlik
        # zaifliklariga olib kelishi mumkin.
        #
        # TO'G'RI YECHIM: Maxsus xavfsiz "sandbox" (qum qutisi) muhitida ishlatish.
        # Buning uchun `restrictedpython` kutubxonasidan foydalanish yoki Piston kabi
        # API orqali alohida xavfsiz servisda kodni ishga tushirish tavsiya etiladi.
        #
        # Hozircha, biz bu amaliyotning xavfliligini ko'rsatish uchun faqat log yozamiz
        # va `async` funksiya ichida kodni bajarishning to'g'ri usulini ko'rsatamiz.

        # Kod bajarilishi uchun mavjud bo'lgan o'zgaruvchilar
        execution_globals = {
            'bot': self.bot,
            'chat_id': chat_id,
            'context': context, # Bu lug'at orqali node'lar o'rtasida ma'lumot almashish mumkin
            'asyncio': asyncio,
            # Xabarga oid o'zgaruvchilar (agar mavjud bo'lsa) context'dan olinadi
            'message': context.get('message'), 
            'callback': context.get('callback_query'),
        }

        try:
            # Asinxron kodni to'g'ri bajarish uchun
            exec_code = f"async def __exec_code():\n"
            exec_code += "".join(f"    {line}\n" for line in python_code.splitlines())
            
            # Kodni lokal scope'da `exec` qilamiz
            exec(exec_code, execution_globals)
            
            # Yaratilgan asinxron funksiyani chaqiramiz
            coro = execution_globals['__exec_code']()
            await coro

            self.logger.info(f"CustomCodeNode kodi muvaffaqiyatli bajarildi (chat_id: {chat_id})")

        except Exception as e:
            error_message = f"Custom code'ni bajarishda xatolik yuz berdi: {e}"
            self.logger.error(error_message, exc_info=True)
            # Xatolik haqida admin yoki foydalanuvchiga xabar berish mumkin
            await self.bot.send_message(chat_id, f"⚠️ Kod bajarishda xatolik:\n<pre>{e}</pre>")
```

### 📄 app/engine/handlers/media_handlers.py

```py
# app/engine/handlers/media_handlers.py
from typing import Dict, Any
from .base import ActionHandler

class SendPhotoHandler(ActionHandler):
    """SendPhotoNode'ni bajarish uchun mas'ul."""
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        source_type = data.get('photoSourceType', 'url')
        photo_id = data.get('photoFileId') if source_type == 'file_id' else data.get('photoUrl')
        
        if not photo_id:
            self.logger.error(f"Node data'da 'photoFileId' yoki 'photoUrl' topilmadi: {data}")
            return
            
        params = self._prepare_common_params(data)
        if data.get('caption'):
            params['caption'] = data.get('caption')
            
        recipient_ids = self._get_recipients(data, chat_id)
        for recipient_id in recipient_ids:
            try:
                await self.bot.send_photo(chat_id=recipient_id, photo=photo_id, **params)
            except Exception as e:
                self.logger.error(f"Rasm yuborishda xatolik (chat_id: {recipient_id}): {e}")

class SendVideoHandler(ActionHandler):
    """SendVideoNode'ni bajarish uchun mas'ul."""
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        source_type = data.get('videoSourceType', 'url')
        video_id = data.get('videoFileId') if source_type == 'file_id' else data.get('videoUrl')

        if not video_id:
            self.logger.error(f"Node data'da 'videoFileId' yoki 'videoUrl' topilmadi: {data}")
            return

        params = self._prepare_common_params(data)
        if data.get('caption'): params['caption'] = data.get('caption')
        if data.get('width'): params['width'] = int(data['width'])
        if data.get('height'): params['height'] = int(data['height'])
        if data.get('duration'): params['duration'] = int(data['duration'])
        if data.get('supportsStreaming'): params['supports_streaming'] = True
        
        recipient_ids = self._get_recipients(data, chat_id)
        for recipient_id in recipient_ids:
            try:
                await self.bot.send_video(chat_id=recipient_id, video=video_id, **params)
            except Exception as e:
                self.logger.error(f"Video yuborishda xatolik (chat_id: {recipient_id}): {e}")

class SendAudioHandler(ActionHandler):
    """SendAudioNode'ni bajarish uchun mas'ul."""
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        source_type = data.get('audioSourceType', 'url')
        audio_id = data.get('audioFileId') if source_type == 'file_id' else data.get('audioUrl')

        if not audio_id:
            self.logger.error(f"Node data'da 'audioFileId' yoki 'audioUrl' topilmadi: {data}")
            return

        params = self._prepare_common_params(data)
        if data.get('caption'): params['caption'] = data.get('caption')
        if data.get('performer'): params['performer'] = data.get('performer')
        if data.get('title'): params['title'] = data.get('title')
        if data.get('duration'): params['duration'] = int(data['duration'])
        
        recipient_ids = self._get_recipients(data, chat_id)
        for recipient_id in recipient_ids:
            try:
                await self.bot.send_audio(chat_id=recipient_id, audio=audio_id, **params)
            except Exception as e:
                self.logger.error(f"Audio yuborishda xatolik (chat_id: {recipient_id}): {e}")

class SendFileHandler(ActionHandler):
    """SendFileNode'ni (document) bajarish uchun mas'ul."""
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        source_type = data.get('fileSourceType', 'url')
        file_id = data.get('fileId') if source_type == 'file_id' else data.get('fileUrl')

        if not file_id:
            self.logger.error(f"Node data'da 'fileId' yoki 'fileUrl' topilmadi: {data}")
            return

        params = self._prepare_common_params(data)
        if data.get('caption'): params['caption'] = data.get('caption')
        
        recipient_ids = self._get_recipients(data, chat_id)
        for recipient_id in recipient_ids:
            try:
                await self.bot.send_document(chat_id=recipient_id, document=file_id, **params)
            except Exception as e:
                self.logger.error(f"Fayl yuborishda xatolik (chat_id: {recipient_id}): {e}")
```

### 📄 app/engine/handlers/message_handlers.py

```py
# app/engine/handlers/message_handlers.py
from typing import Dict, Any
from .base import ActionHandler

class SendTextHandler(ActionHandler):
    """SendTextMessageNode'ni bajarish uchun mas'ul."""

    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        text = data.get('messageText', '[Matn ko\'rsatilmagan]')
        # TODO: Kelajakda `context`dagi o'zgaruvchilarni matnga qo'yish logikasi qo'shiladi.
        # Masalan: text.format(**context)
        
        params = self._prepare_common_params(data)
        
        if data.get('parseMode') and data['parseMode'] != 'None':
            params['parse_mode'] = data['parseMode']
        
        if data.get('disableWebPagePreview'):
            params['disable_web_page_preview'] = data.get('disableWebPagePreview')

        recipient_ids = self._get_recipients(data, chat_id)
        for recipient_id in recipient_ids:
            try:
                await self.bot.send_message(
                    chat_id=recipient_id,
                    text=text,
                    **params
                )
            except Exception as e:
                self.logger.error(f"Xabar yuborishda xatolik (chat_id: {recipient_id}): {e}")
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

### 📄 app/engine/state_manager.py

```py
# app/engine/state_manager.py
from aiogram.fsm.context import FSMContext
from app.engine.fsm import FlowState


class StateManager:
    def __init__(self, fsm_context: FSMContext):
        self.context = fsm_context

    async def set_pause_after_node(self, node_id: str, flow_data: dict):
        """Sxema oqimini aniq bir node'dan keyin 'pauza' qiladi."""
        await self.context.set_state(FlowState.waiting_for_trigger)
        flow_data['paused_after_node_id'] = node_id
        await self.context.set_data(flow_data)

    async def get_paused_node_id(self) -> str | None:
        """Pauza qilingan node'ning ID'sini oladi."""
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
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    ReplyKeyboardRemove
)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

def build_keyboard(keyboard_config: Optional[Dict]) -> Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove]]:
    """
    Frontend'dan kelgan yangi, murakkab keyboard konfiguratsiya obyektidan 
    aiogram uchun klaviatura yasaydi.
    
    keyboard_config = { 
      "active": "inline" | "reply", 
      "inline": [[...]], 
      "reply": [[...]] 
    }
    """
    if not keyboard_config:
        return None

    active_type = keyboard_config.get('active')
    # Aktiv turdagi tugmalar massivini olamiz, masalan 'inline' yoki 'reply'
    buttons_data = keyboard_config.get(active_type)

    if not buttons_data or not isinstance(buttons_data, list) or not any(row for row in buttons_data):
        # Agar aktiv turdagi tugmalar bo'sh bo'lsa (masalan, `[]` yoki `[[]]`),
        # hech narsa qaytarmaymiz. Bu klaviaturani o'zgartirmaslik imkonini beradi.
        return None
        
    # Tugma turini aniqlash uchun birinchi tugmani tekshiramiz
    try:
        # Birinchi qatorning birinchi tugmasini olamiz
        first_button_type = buttons_data[0][0].get('type')
    except (IndexError, AttributeError):
        # Agar tugmalar massivi g'alati formatda bo'lsa
        return None

    # --- Inline Keyboard yasash ---
    if first_button_type in ['url', 'callback']:
        builder = InlineKeyboardBuilder()
        for row in buttons_data:
            buttons_to_add = []
            for btn_data in row:
                # Faqat kerakli maydonlari bor tugmalarni qo'shamiz
                if btn_data.get('text') and btn_data.get('value'):
                    if btn_data['type'] == 'url':
                        buttons_to_add.append(InlineKeyboardButton(text=btn_data['text'], url=btn_data['value']))
                    else: # 'callback'
                        buttons_to_add.append(InlineKeyboardButton(text=btn_data['text'], callback_data=str(btn_data['value'])))
            
            if buttons_to_add:
                builder.row(*buttons_to_add)
        return builder.as_markup()
    
    # --- Reply Keyboard yasash ---
    elif first_button_type in ['reply', 'request_contact', 'request_location']:
        builder = ReplyKeyboardBuilder()
        for row in buttons_data:
            buttons_to_add = []
            for btn_data in row:
                if not btn_data.get('text'):
                    continue
                
                request_contact = btn_data['type'] == 'request_contact'
                request_location = btn_data['type'] == 'request_location'
                
                buttons_to_add.append(KeyboardButton(
                    text=btn_data['text'], 
                    request_contact=request_contact, 
                    request_location=request_location
                ))

            if buttons_to_add:
                builder.row(*buttons_to_add)
        
        # one_time_keyboard=False qilamiz, toki foydalanuvchi bir necha marta bosa olsin.
        # Frontend logikasiga ko'ra bu to'g'ri keladi.
        return builder.as_markup(resize_keyboard=True, one_time_keyboard=False)

    return None
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
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties  # <--- QO'SHILDI: import

from env import BASE_WEBHOOK_URL, BOT_TOKEN, FLOW_FILE_PATH
from app.engine.flow_controller import FlowController
from app.handlers.common import router as common_router


# --- Webhook Sozlamalari (5-qadamda to'ldiriladi) ---
WEBHOOK_PATH = f"/bot/{BOT_TOKEN}"
WEBHOOK_URL = f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}"
# ----------------------------

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


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


# FastAPI welcome page
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

### 📄 env.py

```py
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


```

### 📄 just.py

```py
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart
from aiogram.utils import executor

API_TOKEN = 'YOUR_BOT_TOKEN_HERE'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)

# Keyboard with a button
keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Press me!", callback_data="button_pressed")]
])

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Hello! Press the button or send me a message.", reply_markup=keyboard)

@dp.callback_query()
async def button_handler(callback: types.CallbackQuery):
    await callback.answer("Button pressed!")
    await callback.message.answer("You pressed the button!")

@dp.message()
async def message_handler(message: types.Message):
    await message.reply(f"You said: {message.text}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
```

### 📄 nodes.json

```json
{
  "nodes": [
    {
      "id": "dndnode_1752177694533_2",
      "type": "CommandTriggerNode",
      "position": {
        "x": -3038.845261885198,
        "y": 597.2072670763532
      },
      "data": {
        "command": "/start"
      },
      "width": 320,
      "height": 196,
      "selected": false,
      "dragging": false,
      "positionAbsolute": {
        "x": -3038.845261885198,
        "y": 597.2072670763532
      }
    },
    {
      "id": "dndnode_1752177700013_3",
      "type": "SendTextMessageNode",
      "position": {
        "x": -3214.414199185657,
        "y": 885.2147025463786
      },
      "data": {
        "recipients": {
          "sendToSender": true,
          "additionalIds": []
        },
        "keyboard": {
          "active": "reply",
          "inline": [],
          "reply": [
            [
              {
                "id": "btn-1752177745984",
                "text": "oddiy button",
                "type": "reply"
              },
              {
                "id": "btn-1752177764225",
                "text": "google.com",
                "type": "web_app",
                "webApp": {
                  "url": "https://google.com"
                }
              },
              {
                "id": "btn-1752177765796",
                "text": "📱 Kontaktimni yuborish",
                "type": "request_contact"
              },
              {
                "id": "btn-1752177766564",
                "text": "📍 Joylashuvimni yuborish",
                "type": "request_location"
              }
            ],
            [
              {
                "id": "btn-1752177777604",
                "text": "📊 So'rovnoma yaratish (regular)",
                "type": "request_poll",
                "pollType": "regular"
              },
              {
                "id": "btn-1752177780354",
                "text": "📊 So'rovnoma yaratish (quiz)",
                "type": "request_poll",
                "pollType": "quiz"
              }
            ]
          ]
        },
        "messageText": "Salom oshn",
        "parseMode": "None"
      },
      "width": 400,
      "height": 498,
      "selected": false,
      "dragging": false,
      "positionAbsolute": {
        "x": -3214.414199185657,
        "y": 885.2147025463786
      }
    },
    {
      "id": "dndnode_1752177803088_0",
      "type": "CommandTriggerNode",
      "position": {
        "x": -2430,
        "y": 600
      },
      "data": {
        "command": "/help"
      },
      "width": 320,
      "height": 196,
      "selected": false,
      "dragging": false,
      "positionAbsolute": {
        "x": -2427.5441913576155,
        "y": 600.7865282287377
      }
    },
    {
      "id": "dndnode_1752177803088_1",
      "type": "SendTextMessageNode",
      "position": {
        "x": -2520,
        "y": 890
      },
      "data": {
        "recipients": {
          "sendToSender": true,
          "additionalIds": []
        },
        "keyboard": {
          "active": "inline",
          "inline": [
            [
              {
                "id": "btn-1752177846830",
                "text": "callback buttton",
                "type": "callback",
                "value": "call_back_data"
              },
              {
                "id": "btn-1752177862801",
                "text": "seezntv.uz",
                "type": "callback",
                "value": "https://seezntv.uz"
              },
              {
                "id": "btn-1752177883130",
                "text": "seezntv",
                "type": "url",
                "value": "https://sezntv.uz"
              }
            ],
            [
              {
                "id": "btn-1752177906417",
                "text": "web app seezntv",
                "type": "web_app",
                "webApp": {
                  "url": "https://seezntv.uz"
                }
              }
            ]
          ],
          "reply": [
            [
              {
                "id": "btn-1752177745984",
                "text": "oddiy button",
                "type": "reply"
              },
              {
                "id": "btn-1752177764225",
                "text": "google.com",
                "type": "web_app",
                "webApp": {
                  "url": "https://google.com"
                }
              },
              {
                "id": "btn-1752177765796",
                "text": "📱 Kontaktimni yuborish",
                "type": "request_contact"
              },
              {
                "id": "btn-1752177766564",
                "text": "📍 Joylashuvimni yuborish",
                "type": "request_location"
              }
            ],
            [
              {
                "id": "btn-1752177777604",
                "text": "📊 So'rovnoma yaratish (regular)",
                "type": "request_poll",
                "pollType": "regular"
              },
              {
                "id": "btn-1752177780354",
                "text": "📊 So'rovnoma yaratish (quiz)",
                "type": "request_poll",
                "pollType": "quiz"
              }
            ]
          ]
        },
        "messageText": "Salom oshna",
        "parseMode": "None"
      },
      "width": 400,
      "height": 498,
      "selected": true,
      "dragging": false,
      "positionAbsolute": {
        "x": -2521.716312818528,
        "y": 885.4468153667508
      }
    }
  ],
  "edges": [
    {
      "source": "dndnode_1752177694533_2",
      "sourceHandle": null,
      "target": "dndnode_1752177700013_3",
      "targetHandle": null,
      "type": "smart-edge",
      "style": {
        "strokeWidth": 1.5,
        "stroke": "#495057"
      },
      "animated": false,
      "id": "reactflow__edge-dndnode_1752177694533_2-dndnode_1752177700013_3",
      "selected": false
    },
    {
      "source": "dndnode_1752177803088_0",
      "sourceHandle": null,
      "target": "dndnode_1752177803088_1",
      "targetHandle": null,
      "type": "smart-edge",
      "style": {
        "strokeWidth": 1.5,
        "stroke": "#495057"
      },
      "animated": false,
      "id": "edge-dndnode_1752177803088_0-dndnode_1752177803088_1",
      "selected": false
    }
  ]
}
```

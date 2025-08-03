# Loyiha Tahlili Hisoboti

Sana: 2025-07-05 17:11:10

## 📁 Fayl Strukturasi

```
... Fayl strukturasi bu yerda bo'ladi ...
```

## 📄 Muhim Fayllar Tarkibi

### 📄 .env

```
BOT_TOKEN = "8058205725:AAHiWbWdDl5jnwj_Eqz3NWY8m2itKATkkc8"
NODE_FILE = "flow.json"
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

### 📄 app/_executor.py

```py
import logging
from aiogram import Bot
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
    ReplyKeyboardBuilder,
    KeyboardButton,
    InlineKeyboardButton,
)

class FlowExecutor:
    """
    JSON sxemani qabul qilib, uni Telegram bot logikasi sifatida
    bajaradigan (interpretatsiya qiladigan) asosiy dvijok klassi.
    """

    def __init__(self, flow_data: dict, bot_instance: Bot):
        """
        Dvijokni sxema ma'lumotlari va bot obyekti bilan ishga tushiradi.
        """
        self.flow_data = flow_data
        self.nodes = {node['id']: node for node in self.flow_data.get('nodes', [])}
        self.edges = self._prepare_edges(self.flow_data.get('edges', []))
        self.bot = bot_instance
        logging.info(f"Dvijok {len(self.nodes)} ta node va {len(self.edges)} ta yo'nalish bilan ishga tushdi.")

    def _prepare_edges(self, edges_list: list[dict]) -> dict[str, list]:
        """Qirralarni (edges) tezkor qidirish uchun lug'atga o'tkazadi."""
        edges_map = {}
        for edge in edges_list:
            source_id = edge['source']
            if source_id not in edges_map:
                edges_map[source_id] = []
            edges_map[source_id].append(edge)
        return edges_map

    # --- TRIGGER HANDLER'LAR ---

    async def start_flow_from_message(self, message: Message):
        """Kiruvchi Message'ni qabul qilib, mos triggerdan sxemani boshlaydi."""
        trigger_node = self._find_trigger_for_message(message)
        if not trigger_node:
            logging.warning(f"Message uchun mos trigger topilmadi: {message.text}")
            return

        logging.info(f"Message trigger topildi: {trigger_node['id']}. Sxemani boshlaymiz...")
        await self._traverse_flow(trigger_node, message)

    async def start_flow_from_callback(self, callback: CallbackQuery):
        """Kiruvchi CallbackQuery'ni qabul qilib, mos triggerdan sxemani boshlaydi."""
        trigger_node = self._find_trigger_for_callback(callback)
        if not trigger_node:
            logging.warning(f"Callback uchun mos trigger topilmadi: {callback.data}")
            await callback.answer("Bu tugma uchun amal belgilanmagan.", show_alert=True)
            return

        logging.info(f"Callback trigger topildi: {trigger_node['id']}. Sxemani boshlaymiz...")
        await callback.answer()  # Foydalanuvchi ekranidagi soat belgisini yo'qotish uchun
        await self._traverse_flow(trigger_node, callback)

    # --- TRIGGER QIDIRISH METODLARI ---

    def _find_trigger_for_message(self, message: Message) -> dict | None:
        """Berilgan Message'ga mos keluvchi birinchi trigger node'ni qidiradi."""
        if not message.text:
            return None
        message_text = message.text

        for node in self.nodes.values():
            if node.get('type') == 'MessageTriggerNode':
                data = node.get('data', {})
                context_value = data.get('context', {}).get('value')
                filter_type = data.get('filter')

                if filter_type == 'command' and message_text == context_value:
                    return node
                # --- YANGI QATOR ---
                if filter_type == 'equals' and message_text == context_value:
                    return node
        return None

    def _find_trigger_for_callback(self, callback: CallbackQuery) -> dict | None:
        """Berilgan CallbackQuery'ga mos keluvchi trigger node'ni qidiradi."""
        callback_data_to_find = callback.data
        for node in self.nodes.values():
            # Sxemada callback triggerlari uchun 'ButtonTriggerNode' ishlatamiz
            if node.get('type') == 'ButtonTriggerNode':
                data = node.get('data', {})
                if data.get('callback_data') == callback_data_to_find:
                    return node
        return None

    # --- ASOSIY SXEMA MANTIQI ---

    async def _traverse_flow(self, current_node: dict, trigger_event: Message | CallbackQuery):
        """Sxema bo'ylab yuradi va har bir node amalini bajaradi."""
        if isinstance(trigger_event, Message):
            chat_id = trigger_event.chat.id
        elif isinstance(trigger_event, CallbackQuery):
            chat_id = trigger_event.message.chat.id
        else:
            logging.error(f"Noma'lum trigger turi: {type(trigger_event)}")
            return
        
        while current_node:
            logging.info(f"Bajarilmoqda: Node ID {current_node['id']}, Turi: {current_node['type']}")
            await self._execute_node_action(current_node, chat_id, trigger_event)

            outgoing_edges = self.edges.get(current_node['id'], [])
            if not outgoing_edges:
                logging.info("Sxema tugadi. Keyingi yo'nalish yo'q.")
                break
            
            # Hozircha shartsiz, faqat birinchi yo'nalish bo'ylab ketamiz.
            # Kelajakda ConditionNode uchun bu yerda mantiq murakkablashadi.
            next_edge = outgoing_edges[0]
            current_node = self.nodes.get(next_edge['target'])
            if not current_node:
                logging.error(f"Xatolik: Edge {next_edge.get('id')} ko'rsatgan node {next_edge.get('target')} topilmadi.")
                break

    # --- NODE AMALLARINI BAJARISH ---

    async def _execute_node_action(self, node: dict, chat_id: int, trigger_event: Message | CallbackQuery):
        node_type = node.get('type')
        data = node.get('data', {})

        if node_type == 'SendTextMessageNode':
            text_to_send = data.get('messageText', '[Xabar matni topilmadi]')
            
            # --- YAXSHILANGAN QISM ---
            # Agar 'buttons' maydoni bo'lsa va u bo'sh bo'lsa, klaviaturani o'chiramiz.
            if 'buttons' in data and not data['buttons']:
                keyboard = ReplyKeyboardRemove()
            else:
                keyboard = self._build_keyboard(data.get('buttons'))

            await self.bot.send_message(
                chat_id=chat_id,
                text=text_to_send,
                reply_markup=keyboard
            )
            # --- YAXSHILANGAN QISM TUGADI ---
    
    # --- YORDAMCHI METODLAR ---

    def _build_keyboard(self, buttons_data: list[list[dict]]):
        """
        JSON sxemadagi tugmalar massividan aiogram KeyboardMarkup obyektini yasaydi.
        """
        if not buttons_data or not buttons_data[0]:
            return None # Bu yerda None qaytaramiz, _execute_node_action buni to'g'ri ishlaydi


        # Klaviatura turini birinchi tugmaning tipiga qarab aniqlaymiz.
        # Haqiqiy loyihada 'inline' va 'reply' birga kelmasligini tekshirish kerak.
        first_button_type = buttons_data[0][0].get('type')

        if first_button_type in ['url', 'callback']:
            builder = InlineKeyboardBuilder()
            for row in buttons_data:
                row_buttons = []
                for button_config in row:
                    text = button_config.get('text', '')
                    btn_type = button_config.get('type')
                    value = button_config.get('value', '')

                    if btn_type == 'url' and value:
                        row_buttons.append(InlineKeyboardButton(text=text, url=value))
                    elif btn_type == 'callback' and value:
                        row_buttons.append(InlineKeyboardButton(text=text, callback_data=value))
                if row_buttons:
                    builder.row(*row_buttons)
            return builder.as_markup()
        
        elif first_button_type in ['reply', 'request_contact', 'request_location']:
            builder = ReplyKeyboardBuilder()
            for row in buttons_data:
                row_buttons = []
                for button_config in row:
                    text = button_config.get('text', '')
                    btn_type = button_config.get('type')
                    
                    if btn_type == 'reply':
                        row_buttons.append(KeyboardButton(text=text))
                    elif btn_type == 'request_contact':
                        row_buttons.append(KeyboardButton(text=text, request_contact=True))
                    elif btn_type == 'request_location':
                        row_buttons.append(KeyboardButton(text=text, request_location=True))
                if row_buttons:
                    builder.row(*row_buttons)
            return builder.as_markup(resize_keyboard=True)

        return None
```

### 📄 app/engine/__init__.py

```py

```

### 📄 app/engine/context.py

```py

```

### 📄 app/engine/engine.py

```py
# app/engine/engine.py

import logging
from aiogram import Bot
from aiogram.types import Message, CallbackQuery

from .loader import SchemaLoader
from .triggers import TriggerFinder
from .executors import NodeExecutor
# Hali yaratilmagan, lekin kelajak uchun reja
# from .navigator import FlowNavigator
# from .context import ExecutionContext

class FlowEngine:
    def __init__(self, bot: Bot, flow_file_path: str):
        self.bot = bot
        # 1. Sxemani yuklaymiz
        schema = SchemaLoader(flow_file_path)
        self.nodes = schema.nodes
        self.edges = schema.edges

        # 2. Yordamchi komponentlarni yaratamiz
        self.trigger_finder = TriggerFinder(list(self.nodes.values()))
        self.node_executor = NodeExecutor(bot)
        # self.navigator = FlowNavigator(self.edges) # Kelajakda

    async def handle_message(self, message: Message):
        """Kiruvchi xabarga ishlov beradi."""
        start_node = self.trigger_finder.find_for_message(message)
        if start_node:
            await self._traverse_flow(start_node, message.chat.id)
        else:
            logging.warning(f"Message uchun trigger topilmadi: '{message.text}'")

    async def handle_callback(self, callback: CallbackQuery):
        """Kiruvchi callback'ga ishlov beradi."""
        start_node = self.trigger_finder.find_for_callback(callback)
        if start_node:
            await callback.answer()
            await self._traverse_flow(start_node, callback.message.chat.id)
        else:
            logging.warning(f"Callback uchun trigger topilmadi: '{callback.data}'")
            await callback.answer("Bu tugma uchun amal topilmadi.", show_alert=True)

    async def _traverse_flow(self, current_node: dict, chat_id: int):
        """Sxema bo'ylab yuradi (hozircha shartsiz)."""
        while current_node:
            await self.node_executor.execute(current_node, chat_id)

            # --- KELAJAKDA BU QISM FlowNavigator'ga O'TADI ---
            outgoing_edges = self.edges.get(current_node['id'], [])
            if not outgoing_edges:
                logging.info(f"Sxema tugadi (ID: {current_node['id']}).")
                break

            # Hozircha faqat birinchi yo'nalish
            next_edge = outgoing_edges[0]
            current_node = self.nodes.get(next_edge['target'])
            if not current_node:
                logging.error(f"Target node topilmadi: {next_edge.get('target')}")
                break
```

### 📄 app/engine/executors.py

```py
# app/engine/executors.py

import logging
from typing import Dict
from aiogram import Bot
from aiogram.types import ReplyKeyboardRemove
# Yordamchi keyboard builder'ni ham alohida modulga chiqaramiz
from .utils import build_keyboard

class NodeExecutionError(Exception):
    pass

class NodeExecutor:
    def __init__(self, bot: Bot):
        self.bot = bot
        # Kelajakda bu yerga boshqa turdagi node'lar uchun "handler"lar qo'shiladi
        self._handlers = {
            'SendTextMessageNode': self._handle_send_text_message
        }

    async def execute(self, node: Dict, chat_id: int):
        """Node'ni uning turiga qarab bajaradi."""
        node_type = node.get('type')
        handler = self._handlers.get(node_type)

        if not handler:
            logging.warning(f"Node turi uchun bajaruvchi (handler) topilmadi: {node_type}")
            return

        try:
            logging.info(f"Bajarilmoqda: Node ID {node.get('id')}, Turi: {node_type}")
            await handler(node.get('data', {}), chat_id)
        except Exception as e:
            raise NodeExecutionError(f"Node {node.get('id')} bajarilishida xatolik: {e}")

    # --- HANDLER METODLARI ---
    # Har bir handler faqat o'ziga kerakli 'data' va 'chat_id' ni oladi
    async def _handle_send_text_message(self, data: Dict, chat_id: int):
        """SendTextMessageNode uchun logikani bajaradi."""
        text_to_send = data.get('messageText', '[Xabar matni topilmadi]')

        if 'buttons' in data and not data['buttons']:
            keyboard = ReplyKeyboardRemove()
        else:
            keyboard = build_keyboard(data.get('buttons')) # utils.py dan chaqiramiz

        await self.bot.send_message(
            chat_id=chat_id,
            text=text_to_send,
            reply_markup=keyboard
        )

# Yordamchi funksiyalarni utils.py ga chiqaramiz
# app/engine/utils.py
# ... _build_keyboard funksiyasining kodi shu yerda bo'ladi ...
```

### 📄 app/engine/loader.py

```py
import json
from typing import Dict, List

class SchemaError(Exception):
    """Sxemadagi xatoliklar uchun maxsus exception."""
    pass

class SchemaLoader:
    def __init__(self, flow_file_path: str):
        self.flow_file_path = flow_file_path
        self.nodes: Dict[str, Dict] = {}
        self.edges: Dict[str, List[Dict]] = {}
        self._load_and_validate()

    def _load_and_validate(self):
        """Faylni yuklaydi va oddiy validatsiyadan o'tkazadi."""
        try:
            with open(self.flow_file_path, 'r', encoding='utf-8') as f:
                flow_data = json.load(f)
        except FileNotFoundError:
            raise SchemaError(f"Sxema fayli topilmadi: {self.flow_file_path}")
        except json.JSONDecodeError:
            raise SchemaError(f"Sxema fayli yaroqsiz JSON formatida: {self.flow_file_path}")

        # Validatsiya (KISS - oddiy va tushunarli)
        if 'nodes' not in flow_data or 'edges' not in flow_data:
            raise SchemaError("Sxemada 'nodes' yoki 'edges' maydonlari mavjud emas.")

        # DRY - kod takrorlanishini oldini olish
        self.nodes = self._prepare_nodes(flow_data.get('nodes', []))
        self.edges = self._prepare_edges(flow_data.get('edges', []))

    @staticmethod
    def _prepare_nodes(nodes_list: List[Dict]) -> Dict[str, Dict]:
        """Node'larni tezkor qidirish uchun lug'atga o'tkazadi."""
        return {node['id']: node for node in nodes_list}

    @staticmethod
    def _prepare_edges(edges_list: List[Dict]) -> Dict[str, List[Dict]]:
        """Qirralarni (edges) source_id bo'yicha guruhlaydi."""
        edges_map = {}
        for edge in edges_list:
            source_id = edge['source']
            if source_id not in edges_map:
                edges_map[source_id] = []
            edges_map[source_id].append(edge)
        return edges_map
```

### 📄 app/engine/navigator.py

```py

```

### 📄 app/engine/triggers.py

```py
from typing import Dict, Optional, List
from aiogram.types import Message, CallbackQuery

class TriggerFinder:
    def __init__(self, nodes: List[Dict]):
        # Faqat trigger node'larni saqlab olamiz, optimizatsiya uchun
        self.trigger_nodes = [node for node in nodes if 'Trigger' in node.get('type', '')]

    def find_for_message(self, message: Message) -> Optional[Dict]:
        """Berilgan Message'ga mos keluvchi trigger'ni qidiradi."""
        if not message.text:
            return None
        message_text = message.text

        for node in self.trigger_nodes:
            if node.get('type') == 'MessageTriggerNode':
                data = node.get('data', {})
                context_value = data.get('context', {}).get('value')
                filter_type = data.get('filter')

                # Bu yerni kelajakda murakkablashtirish mumkin
                if filter_type == 'command' and message_text == context_value:
                    return node
                if filter_type == 'equals' and message_text == context_value:
                    return node
        return None

    def find_for_callback(self, callback: CallbackQuery) -> Optional[Dict]:
        """Berilgan CallbackQuery'ga mos keluvchi trigger'ni qidiradi."""
        callback_data = callback.data
        for node in self.trigger_nodes:
            if node.get('type') == 'ButtonTriggerNode':
                data = node.get('data', {})
                if data.get('callback_data') == callback_data:
                    return node
        return None
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

def build_keyboard(
    buttons_data: Optional[List[List[Dict]]]
) -> Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove]]:
    """
    JSON sxemadagi tugmalar massividan aiogram KeyboardMarkup obyektini yasaydi.

    Bu funksiya SOLID tamoyillariga mos ravishda bitta vazifani bajaradi:
    ma'lumotlar strukturasini aiogram obyektiga o'girish.

    Args:
        buttons_data: Qatorlar va tugmalardan iborat list.
                      Masalan: [[{'text': 'Btn1'}, {'text': 'Btn2'}], [{'text': 'Btn3'}]]

    Returns:
        - aiogram klaviatura obyekti (InlineKeyboardMarkup yoki ReplyKeyboardMarkup).
        - Agar `buttons_data` bo'sh list (`[]`) bo'lsa, ReplyKeyboardRemove.
        - Agar `buttons_data` None yoki bo'sh qatorlardan iborat bo'lsa, None.
    """
    if buttons_data is None:
        return None
    
    # Agar bo'sh list uzatilsa, bu klaviaturani o'chirish kerakligini bildiradi.
    if not buttons_data:
        return ReplyKeyboardRemove()
    
    # Agar ichidagi list bo'sh bo'lsa, hech qanday klaviatura kerak emas.
    if not any(buttons_data):
        return None

    # Klaviatura turini birinchi tugmaning tipiga qarab aniqlaymiz.
    # Bu yondashuv (KISS) oddiy, lekin kelajakda inline va reply
    # tugmalarining birga kelmasligini tekshirish uchun validatsiya qo'shish mumkin.
    try:
        first_button_type = buttons_data[0][0].get('type')
    except (IndexError, AttributeError):
        # Tugmalar strukturasi noto'g'ri bo'lsa
        return None

    if first_button_type in ['url', 'callback']:
        return _build_inline_keyboard(buttons_data)
    
    elif first_button_type in ['reply', 'request_contact', 'request_location']:
        return _build_reply_keyboard(buttons_data)

    return None

def _build_inline_keyboard(buttons_data: List[List[Dict]]) -> InlineKeyboardMarkup:
    """Inline klaviatura yasaydi."""
    builder = InlineKeyboardBuilder()
    for row in buttons_data:
        row_buttons = []
        for button_config in row:
            text = button_config.get('text', '')
            btn_type = button_config.get('type')
            value = button_config.get('value', '')

            if not text:
                continue # Matni yo'q tugmani o'tkazib yuboramiz

            if btn_type == 'url' and value:
                row_buttons.append(InlineKeyboardButton(text=text, url=value))
            elif btn_type == 'callback' and value:
                row_buttons.append(InlineKeyboardButton(text=text, callback_data=value))
        
        if row_buttons:
            # `builder.row()` metodi argumentlarni alohida-alohida qabul qiladi,
            # shuning uchun `*` (unpack) operatoridan foydalanamiz.
            builder.row(*row_buttons)
            
    return builder.as_markup()

def _build_reply_keyboard(buttons_data: List[List[Dict]]) -> ReplyKeyboardMarkup:
    """Reply (oddiy) klaviatura yasaydi."""
    builder = ReplyKeyboardBuilder()
    for row in buttons_data:
        row_buttons = []
        for button_config in row:
            text = button_config.get('text', '')
            btn_type = button_config.get('type')

            if not text:
                continue

            if btn_type == 'reply':
                row_buttons.append(KeyboardButton(text=text))
            elif btn_type == 'request_contact':
                row_buttons.append(KeyboardButton(text=text, request_contact=True))
            elif btn_type == 'request_location':
                row_buttons.append(KeyboardButton(text=text, request_location=True))
        
        if row_buttons:
            builder.row(*row_buttons)

    # `resize_keyboard=True` klaviaturani ixchamroq qiladi.
    # `one_time_keyboard` True bo'lsa, tugma bosilgach klaviatura yo'qoladi.
    # Buni ham kelajakda JSON'dan boshqarish mumkin.
    return builder.as_markup(resize_keyboard=True)
```

### 📄 app/handlers.py

```py
# app/handlers.py (TO'G'RILANGAN KOD)

from aiogram import Router
from aiogram.types import Message, CallbackQuery
from app.engine.engine import FlowEngine # <--- To'g'ri klassni import qilamiz

router = Router()

@router.message()
async def universal_message_handler(message: Message, engine: FlowEngine): # <--- MUHIM O'ZGARISH
    """Barcha kiruvchi xabarlarni qabul qilib, dvijokka uzatadi."""
    await engine.handle_message(message)

@router.callback_query()
async def universal_callback_handler(callback: CallbackQuery, engine: FlowEngine): # <--- MUHIM O'ZGARISH
    """Barcha kiruvchi callback'larni qabul qilib, dvijokka uzatadi."""
    await engine.handle_callback(callback)
```

### 📄 app/main.py

```py
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

from env import BOT_TOKEN, FLOW_FILE_PATH  # Token va flow fayl yo'li

from app.engine.engine import FlowEngine  # FlowEngine import
from app.handlers import router as bot_router  # Router import

# --- Webhook Sozlamalari ---
BASE_WEBHOOK_URL = "https://3fe4-185-139-137-7.ngrok-free.app"  # O'zingizning manzilingizni kiriting
WEBHOOK_PATH = f"/bot/{BOT_TOKEN}"
WEBHOOK_URL = f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}"
# ----------------------------

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Ilova ishga tushmoqda...")

    try:
        # Bot va dvigatelni yaratish
        bot = Bot(token=BOT_TOKEN)
        engine = FlowEngine(bot=bot, flow_file_path=FLOW_FILE_PATH)

        # Dispatcher yaratish, engine ni 'engine' kaliti bilan uzatish
        dp = Dispatcher(storage=MemoryStorage(), engine=engine)
        dp.include_router(bot_router)

        # Holatga saqlash
        app.state.bot = bot
        app.state.dispatcher = dp

        # Webhook o‘rnatish
        await bot.set_webhook(url=WEBHOOK_URL)
        logging.info(f"Webhook o'rnatildi: {WEBHOOK_URL}")

        yield  # Ilova ishida davom etish

    except Exception as e:
        logging.critical(f"Kritik xato, ilova ishga tushmadi: {e}", exc_info=True)
        yield  # Xato bo‘lsa ham finally qismiga o‘tadi

    finally:
        logging.info("Ilova to'xtamoqda...")
        if hasattr(app.state, 'bot') and app.state.bot:
            await app.state.bot.delete_webhook()
            await app.state.bot.session.close()
            logging.info("Webhook o'chirildi va sessiya yopildi.")


app = FastAPI(lifespan=lifespan)

@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    dp = app.state.dispatcher
    bot = app.state.bot

    telegram_update = types.Update(**update)
    try:
        await dp.feed_update(bot=bot, update=telegram_update)
    except Exception as e:
        logging.error(f"Update'ni qayta ishlashda xatolik: {e}", exc_info=True)

    return {'status': 'ok'}
```

### 📄 env.py

```py
import os
import dotenv

dotenv.load_dotenv('.env', override=True)

BOT_TOKEN = os.getenv('BOT_TOKEN')
FLOW_FILE_PATH = os.getenv('NODE_FILE')
```

### 📄 flow.json

```json
{
  "nodes": [
    {
      "id": "node_start_trigger",
      "type": "MessageTriggerNode",
      "data": { "filter": "command", "context": { "value": "/start" } }
    },
    {
      "id": "node_show_reply_keyboard",
      "type": "SendTextMessageNode",
      "data": {
        "messageText": "Assalomu alaykum! Quyidagi menyudan tanlang:",
        "buttons": [
          [
            { "id": "btn_reply_1", "text": "Mening profilim", "type": "reply" },
            { "id": "btn_reply_2", "text": "Sozlamalar", "type": "reply" }
          ],
          [
            {
              "id": "btn_reply_close",
              "text": "/close keyboard",
              "type": "reply"
            }
          ]
        ]
      }
    },
    {
      "id": "node_profile_trigger",
      "type": "MessageTriggerNode",
      "data": { "filter": "equals", "context": { "value": "Mening profilim" } }
    },
    {
      "id": "node_profile_action",
      "type": "SendTextMessageNode",
      "data": {
        "messageText": "Bu sizning profilingiz haqidagi ma'lumotlar..."
      }
    },
    {
      "id": "node_close_trigger",
      "type": "MessageTriggerNode",
      "data": { "filter": "equals", "context": { "value": "/close keyboard" } }
    },
    {
      "id": "node_close_action",
      "type": "SendTextMessageNode",
      "data": {
        "messageText": "Klaviatura yopildi.",
        "buttons": []
      }
    }
  ],
  "edges": [
    {
      "source": "node_start_trigger",
      "target": "node_show_reply_keyboard",
      "id": "edge_1"
    },
    {
      "source": "node_profile_trigger",
      "target": "node_profile_action",
      "id": "edge_2"
    },
    {
      "source": "node_close_trigger",
      "target": "node_close_action",
      "id": "edge_3"
    }
  ]
}

```

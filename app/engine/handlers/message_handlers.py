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
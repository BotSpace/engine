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
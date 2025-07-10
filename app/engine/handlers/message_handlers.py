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
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
import json
import logging
from aiogram import Bot
from aiogram.types import Update, Message


class FlowExecutor:
    def __init__(self, flow_data: dict, bot_instance: Bot):
        """
        Dvijokni sxema ma'lumotlari va bot obyekti bilan ishga tushiradi.
        """
        self.nodes = {node['id']: node for node in flow_data.get('nodes', [])}
        self.edges = self._prepare_edges(flow_data.get('edges', []))
        self.bot = bot_instance
        logging.info(f"Dvijok {len(self.nodes)} ta node va {len(self.edges)} ta yo'nalish bilan ishga tushdi.")

    def _prepare_edges(self, edges_list: list) -> dict:
        """Qirralarni tezkor qidirish uchun lug'atga o'tkazadi."""
        edges_map = {}
        for edge in edges_list:
            source_id = edge['source']
            if source_id not in edges_map:
                edges_map[source_id] = []
            edges_map[source_id].append(edge)
        return edges_map

    async def start_flow_from_message(self, message: Message):
        """
        Kiruvchi Message'ni qabul qilib, mos triggerdan sxemani boshlaydi.
        """
        trigger_node = self._find_trigger_for_message(message)
        
        if not trigger_node:
            logging.warning(f"Message uchun mos trigger topilmadi: {message.text}")
            return

        logging.info(f"Trigger topildi: {trigger_node['id']}. Sxemani boshlaymiz...")
        # _traverse_flow'ga butun message'ni uzatamiz
        await self._traverse_flow(trigger_node, message)

        
    def _find_trigger_for_message(self, message: Message) -> dict | None:
        """Berilgan Message'ga mos keluvchi birinchi trigger node'ni qidiradi."""
        if not message.text:
            return None

        message_text = message.text
        
        for node in self.nodes.values():
            if node.get('type') == 'MessageTriggerNode':
                data = node.get('data', {})
                context_value = data.get('context', {}).get('value')
                
                if data.get('filter') == 'command' and message_text == context_value:
                    return node
        return None


    async def _traverse_flow(self, current_node: dict, trigger_event: Message):
        """Sxema bo'ylab yuradi va har bir node amalini bajaradi."""
        # Chat ID'ni trigger bo'lgan event'dan olamiz
        chat_id = trigger_event.chat.id
        
        while current_node:
            logging.info(f"Bajarilmoqda: Node ID {current_node['id']}, Turi: {current_node['type']}")
            # _execute_node_action'ga ham trigger_event'ni uzatamiz
            await self._execute_node_action(current_node, chat_id, trigger_event)

            # Keyingi node'ga o'tish
            outgoing_edges = self.edges.get(current_node['id'], [])
            if not outgoing_edges:
                logging.info("Sxema tugadi. Keyingi yo'nalish yo'q.")
                break
            
            next_edge = outgoing_edges[0]
            current_node = self.nodes.get(next_edge['target'])
            if not current_node:
                logging.error(f"Xatolik: Edge {next_edge['id']} ko'rsatgan node {next_edge['target']} topilmadi.")
                break

            
    async def _execute_node_action(self, node: dict, chat_id: int, trigger_event: Message):
        """Node'ning turiga qarab tegishli amalni bajaradi."""
        node_type = node.get('type')
        data = node.get('data', {})

        if node_type == 'SendTextMessageNode':
            text_to_send = data.get('messageText', '[Xabar matni topilmadi]')
            await self.bot.send_message(chat_id=chat_id, text=text_to_send)
            
        # ...boshqa barcha node turlari uchun elif bloklari...
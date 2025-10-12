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
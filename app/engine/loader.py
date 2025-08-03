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
# app/engine/state_manager.py
from aiogram.fsm.context import FSMContext
from app.engine.fsm import FlowState

class StateManager:
    def __init__(self, fsm_context: FSMContext):
        self.context = fsm_context

    async def set_pause_after_node(self, node_id: str, flow_data: dict):
        await self.context.set_state(FlowState.waiting_for_trigger)
        flow_data['paused_after_node_id'] = node_id
        await self.context.set_data(flow_data)

    async def get_paused_node_id(self) -> str | None:
        data = await self.context.get_data()
        return data.get("paused_after_node_id")

    async def clear_state(self):
        await self.context.clear()
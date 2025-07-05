from aiogram.fsm.context import FSMContext
from app.engine.fsm import FlowState

class StateManager:
    def __init__(self, fsm_context: FSMContext):
        self.context = fsm_context

    async def set_wait_for_trigger(self, node_id: str):
        await self.context.set_state(FlowState.waiting_for_trigger)
        await self.context.update_data(waiting_for_node_id=node_id)

    async def get_waiting_node_id(self) -> str | None:
        data = await self.context.get_data()
        return data.get("waiting_for_node_id")

    async def clear_state(self):
        await self.context.clear()
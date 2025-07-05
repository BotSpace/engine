from aiogram.fsm.state import State, StatesGroup

class FlowState(StatesGroup):
    waiting_for_trigger = State()
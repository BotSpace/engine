# app/handlers/common.py
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from app.engine.flow_controller import FlowController
from app.engine.fsm import FlowState

router = Router()

# Bu handler foydalanuvchi FlowState.waiting_for_trigger holatida bo'lganda ishlaydi.
# state=... o'rniga StateFilter(...) ishlatiladi.
@router.message(F.content_type.ANY, StateFilter(FlowState.waiting_for_trigger))
@router.callback_query(StateFilter(FlowState.waiting_for_trigger))
async def waiting_handler(update: Message | CallbackQuery, controller: FlowController, state: FSMContext):
    await controller.handle_update(update, state)

# Bu handler foydalanuvchi holati bo'sh (None) bo'lganda ishlaydi.
@router.message(F.content_type.ANY, StateFilter(None))
@router.callback_query(StateFilter(None))
async def initial_handler(update: Message | CallbackQuery, controller: FlowController, state: FSMContext):
    await controller.handle_update(update, state)
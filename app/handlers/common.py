# app/handlers/common.py
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from app.engine.flow_controller import FlowController
from app.engine.fsm import FlowState
from app.repository import create_user_not_exists

router = Router()


@router.message(F.content_type.ANY, StateFilter(FlowState.waiting_for_trigger))
@router.callback_query(StateFilter(FlowState.waiting_for_trigger))
async def waiting_handler(
    update: Message | CallbackQuery, controller: FlowController, state: FSMContext
):
    await controller.handle_update(update, state)


@router.message(F.content_type.ANY, StateFilter(None))
@router.callback_query(StateFilter(None))
async def initial_handler(
    update: Message | CallbackQuery, controller: FlowController, state: FSMContext
):
    if isinstance(update, Message):
        if update.text == "/start":
            first_name = (
                getattr(update.from_user, "first_name", "") if update.from_user else ""
            )
            last_name = (
                getattr(update.from_user, "last_name", "") if update.from_user else ""
            )
            await create_user_not_exists(
                update.chat.id, first_name, last_name
            )  # type:ignore
    await controller.handle_update(update, state)

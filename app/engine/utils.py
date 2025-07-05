from typing import List, Dict, Optional, Union
from aiogram.types import (
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    ReplyKeyboardRemove
)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

def build_keyboard(buttons_data: Optional[List[List[Dict]]]) -> Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove]]:
    if buttons_data is None: return None
    if not buttons_data: return ReplyKeyboardRemove()
    if not any(row for row in buttons_data): return None

    try:
        first_button_type = buttons_data[0][0].get('type')
    except (IndexError, AttributeError):
        return None

    if first_button_type in ['url', 'callback']:
        builder = InlineKeyboardBuilder()
        for row in buttons_data:
            buttons = [
                InlineKeyboardButton(text=btn['text'], url=btn.get('value')) if btn['type'] == 'url'
                else InlineKeyboardButton(text=btn['text'], callback_data=str(btn.get('value')))
                for btn in row if btn.get('text') and btn.get('value')
            ]
            if buttons: builder.row(*buttons)
        return builder.as_markup()
    
    elif first_button_type in ['reply', 'request_contact', 'request_location']:
        builder = ReplyKeyboardBuilder()
        for row in buttons_data:
            buttons = []
            for btn in row:
                if not btn.get('text'): continue
                request_contact = btn['type'] == 'request_contact'
                request_location = btn['type'] == 'request_location'
                buttons.append(KeyboardButton(
                    text=btn['text'], 
                    request_contact=request_contact, 
                    request_location=request_location
                ))
            if buttons: builder.row(*buttons)
        return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

    return None
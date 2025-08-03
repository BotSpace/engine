from typing import List, Dict, Optional, Union
from aiogram.types import (
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    ReplyKeyboardRemove
)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

def build_keyboard(
    buttons_data: Optional[List[List[Dict]]]
) -> Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove]]:
    """
    JSON sxemadagi tugmalar massividan aiogram KeyboardMarkup obyektini yasaydi.

    Bu funksiya SOLID tamoyillariga mos ravishda bitta vazifani bajaradi:
    ma'lumotlar strukturasini aiogram obyektiga o'girish.

    Args:
        buttons_data: Qatorlar va tugmalardan iborat list.
                      Masalan: [[{'text': 'Btn1'}, {'text': 'Btn2'}], [{'text': 'Btn3'}]]

    Returns:
        - aiogram klaviatura obyekti (InlineKeyboardMarkup yoki ReplyKeyboardMarkup).
        - Agar `buttons_data` bo'sh list (`[]`) bo'lsa, ReplyKeyboardRemove.
        - Agar `buttons_data` None yoki bo'sh qatorlardan iborat bo'lsa, None.
    """
    if buttons_data is None:
        return None
    
    # Agar bo'sh list uzatilsa, bu klaviaturani o'chirish kerakligini bildiradi.
    if not buttons_data:
        return ReplyKeyboardRemove()
    
    # Agar ichidagi list bo'sh bo'lsa, hech qanday klaviatura kerak emas.
    if not any(buttons_data):
        return None

    # Klaviatura turini birinchi tugmaning tipiga qarab aniqlaymiz.
    # Bu yondashuv (KISS) oddiy, lekin kelajakda inline va reply
    # tugmalarining birga kelmasligini tekshirish uchun validatsiya qo'shish mumkin.
    try:
        first_button_type = buttons_data[0][0].get('type')
    except (IndexError, AttributeError):
        # Tugmalar strukturasi noto'g'ri bo'lsa
        return None

    if first_button_type in ['url', 'callback']:
        return _build_inline_keyboard(buttons_data)
    
    elif first_button_type in ['reply', 'request_contact', 'request_location']:
        return _build_reply_keyboard(buttons_data)

    return None

def _build_inline_keyboard(buttons_data: List[List[Dict]]) -> InlineKeyboardMarkup:
    """Inline klaviatura yasaydi."""
    builder = InlineKeyboardBuilder()
    for row in buttons_data:
        row_buttons = []
        for button_config in row:
            text = button_config.get('text', '')
            btn_type = button_config.get('type')
            value = button_config.get('value', '')

            if not text:
                continue # Matni yo'q tugmani o'tkazib yuboramiz

            if btn_type == 'url' and value:
                row_buttons.append(InlineKeyboardButton(text=text, url=value))
            elif btn_type == 'callback' and value:
                row_buttons.append(InlineKeyboardButton(text=text, callback_data=value))
        
        if row_buttons:
            # `builder.row()` metodi argumentlarni alohida-alohida qabul qiladi,
            # shuning uchun `*` (unpack) operatoridan foydalanamiz.
            builder.row(*row_buttons)
            
    return builder.as_markup()

def _build_reply_keyboard(buttons_data: List[List[Dict]]) -> ReplyKeyboardMarkup:
    """Reply (oddiy) klaviatura yasaydi."""
    builder = ReplyKeyboardBuilder()
    for row in buttons_data:
        row_buttons = []
        for button_config in row:
            text = button_config.get('text', '')
            btn_type = button_config.get('type')

            if not text:
                continue

            if btn_type == 'reply':
                row_buttons.append(KeyboardButton(text=text))
            elif btn_type == 'request_contact':
                row_buttons.append(KeyboardButton(text=text, request_contact=True))
            elif btn_type == 'request_location':
                row_buttons.append(KeyboardButton(text=text, request_location=True))
        
        if row_buttons:
            builder.row(*row_buttons)

    # `resize_keyboard=True` klaviaturani ixchamroq qiladi.
    # `one_time_keyboard` True bo'lsa, tugma bosilgach klaviatura yo'qoladi.
    # Buni ham kelajakda JSON'dan boshqarish mumkin.
    return builder.as_markup(resize_keyboard=True)
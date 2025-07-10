# app/engine/utils.py
from typing import Dict, Optional, Union
from aiogram.types import (
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    ReplyKeyboardRemove,
    WebAppInfo, # <--- QO'SHILDI
    KeyboardButtonPollType # <--- QO'SHILDI
)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

def build_keyboard(keyboard_config: Optional[Dict]) -> Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove]]:
    """
    Frontend'dan kelgan yangi, murakkab keyboard konfiguratsiya obyektidan 
    aiogram uchun klaviatura yasaydi.
    """
    if not keyboard_config:
        return None

    active_type = keyboard_config.get('active')
    buttons_data = keyboard_config.get(active_type)

    if not buttons_data or not isinstance(buttons_data, list) or not any(row for row in buttons_data):
        return None
        
    try:
        first_button_type = buttons_data[0][0].get('type')
    except (IndexError, AttributeError):
        return None

    # --- Inline Keyboard yasash ---
    if first_button_type in ['url', 'callback', 'web_app']: # <--- 'web_app' QO'SHILDI
        builder = InlineKeyboardBuilder()
        for row in buttons_data:
            buttons_to_add = []
            for btn_data in row:
                btn_type = btn_data.get('type')
                btn_text = btn_data.get('text')
                
                if not btn_text: continue

                if btn_type == 'url' and btn_data.get('value'):
                    buttons_to_add.append(InlineKeyboardButton(text=btn_text, url=btn_data['value']))
                elif btn_type == 'callback' and btn_data.get('value'):
                    buttons_to_add.append(InlineKeyboardButton(text=btn_text, callback_data=str(btn_data['value'])))
                # --- YANGI KOD ---
                elif btn_type == 'web_app' and btn_data.get('webApp', {}).get('url'):
                    web_app_url = btn_data['webApp']['url']
                    buttons_to_add.append(InlineKeyboardButton(text=btn_text, web_app=WebAppInfo(url=web_app_url)))
                # --- KOD TUGADI ---
            
            if buttons_to_add:
                builder.row(*buttons_to_add)
        return builder.as_markup()
    
    # --- Reply Keyboard yasash ---
    elif first_button_type in ['reply', 'request_contact', 'request_location', 'web_app', 'request_poll']: # <--- QO'SHILDI
        builder = ReplyKeyboardBuilder()
        for row in buttons_data:
            buttons_to_add = []
            for btn_data in row:
                if not btn_data.get('text'):
                    continue
                
                btn_type = btn_data.get('type')
                
                # --- YANGI VA O'ZGARTIRILGAN KOD ---
                params = {"text": btn_data['text']}
                if btn_type == 'request_contact':
                    params['request_contact'] = True
                elif btn_type == 'request_location':
                    params['request_location'] = True
                elif btn_type == 'web_app' and btn_data.get('webApp', {}).get('url'):
                    params['web_app'] = WebAppInfo(url=btn_data['webApp']['url'])
                elif btn_type == 'request_poll' and btn_data.get('pollType'):
                    params['request_poll'] = KeyboardButtonPollType(type=btn_data['pollType'])
                
                buttons_to_add.append(KeyboardButton(**params))
                # --- KOD TUGADI ---

            if buttons_to_add:
                builder.row(*buttons_to_add)
        
        return builder.as_markup(resize_keyboard=True, one_time_keyboard=False)

    return None
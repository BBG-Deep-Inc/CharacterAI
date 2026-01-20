from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import os
import sys


current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir) 

sys.path.insert(0, project_root)


from backend.database.character_ai_database.character_core import get_user_models_2

main_keyborad = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = "Profile"),KeyboardButton(text = "Chat")]
])

profile_key_board = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "Subscribe")]
])

subscribe_keyboard = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "Buy subscribtion"),InlineKeyboardButton(text = "Back")]
])

async def create_charccter_keyboead(username:str) -> ReplyKeyboardMarkup:
    user_models = await get_user_models_2(username)
    user_models_name = list(user_models.keys()) 
    result_keybord = ReplyKeyboardMarkup(resize_keyboard=True,row_width = 2)
    for name in user_models_name:
        result_keybord.add(KeyboardButton(name))
    result_keybord.add(KeyboardButton(text = "Back"))    
    return result_keybord    
    
    


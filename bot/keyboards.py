from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton


main_keyborad = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = "Profile"),KeyboardButton(text = "Chat")]
])

profile_key_board = InlineKeyboardMarkup(inline_keyborad = [
    [InlineKeyboardButton(text = "Subscribe")]
])
from loader import db
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_function(btn_name, row_width):
    btn_name = InlineKeyboardMarkup(row_width=row_width)
    categories = db.select_categories()
    for item in categories:
        text = item[0]
        callback_data = item[1]
        btn_name.insert(
            InlineKeyboardButton(text=text, callback_data=callback_data)
        )
    return btn_name

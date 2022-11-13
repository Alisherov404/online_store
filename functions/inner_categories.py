from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def inner_categories_function(btn_name, row_width, data_base):
    btn_name = InlineKeyboardMarkup(row_width=row_width)
    for item in data_base:
        text = item[0]
        callback_data = item[1]
        btn_name.insert(
            InlineKeyboardButton(
                text=text, callback_data=callback_data
            )
        )
    return btn_name

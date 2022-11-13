from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


introduction_btn = InlineKeyboardMarkup(row_width=2)

introduction_btn.insert(
    InlineKeyboardButton(text='Products catalog', callback_data='catalog'),
    InlineKeyboardButton(text='Search', callback_data='search'),
    InlineKeyboardButton(text='')
)

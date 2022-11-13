import sqlite3
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, db, bot
from data.config import ADMINS

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
categories_callbacks = {}

@dp.message_handler(commands=['start'], state='*')
async def bot_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    name = message.from_user.full_name
    apple_logo = 'https://images.idgesg.net/images/article/2020/12/app-store-best-of-2020-100869156-large.jpg?auto=webp&quality=85,70'
    categories_btn = InlineKeyboardMarkup(row_width=2)

    # Add user to database
    categories_btn.row(
        InlineKeyboardButton(text='All product categories 🗓', callback_data='all_product_categories')
    )
    categories_btn.row(
        InlineKeyboardButton(text='Cart 🛒', callback_data='cart'),
        InlineKeyboardButton(text='Search 🔎', callback_data='search')
    )
    categories_btn.row(
        InlineKeyboardButton(text='Apple.com', url='https://www.apple.com/store')
    )
    
    await message.answer_photo(photo=apple_logo, caption=f'@{message.from_user.username}! Welcome to our Apple store bot. Good luck by shopping ✌️', reply_markup=categories_btn)

    # Give info to admin
    count_users = db.count_users()[0]
    person_or_people = 'person'
    if count_users > 1:
        person_or_people = 'people'
    message = f"{message.from_user.full_name} joined to database.\n In database have {count_users} {person_or_people}."
    await bot.send_message(chat_id=ADMINS[0], text=message)


    categories_callbacks.update({
        'categories_callback_data': db.select_categories_callback_data()
    })
    print(db.select_categories_callback_data())
    await state.update_data({
        'categories_callback_data': db.select_categories_callback_data()
    })
    try:
        db.add_step(id=user_id)
    except Exception as error:
        print(error)
    try:
        db.update_step(id=user_id, step=0)
    except Exception:
        pass
    await state.update_data({
         f"{user_id}_step": 0
    })
    await state.update_data({
        f"inner_categories": db.select_all_inner_categories()
    })

    try:
        db.add_user(id=user_id,
                name=name)
    except Exception as error:
        print(error)


from loader import db, dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from states.main import main
from ..commands.start import categories_callbacks


@dp.callback_query_handler(lambda call: [item[0] for item in categories_callbacks['categories_callback_data']] is not None and call.data in [item[0] for item in categories_callbacks['categories_callback_data']], state='*')
async def inner_categories(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    try:
        step = db.select_step(id=user_id)[1]
        inner_categories_btn = InlineKeyboardMarkup(row_width=2)
        inner_categories = db.select_inner_categories(main_callback_data=call.data)

        img = inner_categories[step][0]
        text = inner_categories[step][2]

        inner_categories_btn.row(
            InlineKeyboardButton(text='⬅️', callback_data='left'),
            InlineKeyboardButton(text='❌', callback_data='del'),
            InlineKeyboardButton(text='➡️', callback_data='right')
        )
        inner_categories_btn.row(
            InlineKeyboardButton(text='Cart 🛒', callback_data='cart'),
            InlineKeyboardButton(text='About... ✅', callback_data='about')
        )
        inner_categories_btn.add(
            InlineKeyboardButton(text='🔙 Back', callback_data='back')
        )

        await call.message.delete()
        await call.message.answer_photo(photo=img, caption=text, reply_markup=inner_categories_btn)
        await main.categories.set()
        await state.update_data({
            'main_categories': call.data
        })
    except Exception as error:
        print(error)

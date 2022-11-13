from loader import db, dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from functions.inner_categories import inner_categories_function

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@dp.callback_query_handler(lambda call: call.data == 'all_product_categories', state='*')
async def all_product_categories_call_handler(call: types.CallbackQuery, state: FSMContext):
    try:
        categories = db.select_categories()
        all_inner_categories_btn = InlineKeyboardMarkup(row_width=2)
        all_inner_categories_btn = inner_categories_function(all_inner_categories_btn, 2, categories)
        buttons = await state.get_data()
        all_inner_categories_btn.row(
            InlineKeyboardButton(text='Cart 🛒', callback_data='cart'),
            InlineKeyboardButton(text='All products 🗓', callback_data='all_products')
        )
        all_inner_categories_btn.add(
            InlineKeyboardButton(text='🔙 Back', callback_data='back')
        )

        await call.message.delete()
        await call.message.answer('All product categories list by Apple store. Wait new products 😉', reply_markup=all_inner_categories_btn)
    except Exception as error:
        print(error)

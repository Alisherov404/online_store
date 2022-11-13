from aiogram import types
from loader import dp
from aiogram.types import InlineKeyboardMarkup
from states.main import main
from aiogram.dispatcher import FSMContext
from functions.main_menu import main_menu_function


@dp.callback_query_handler(lambda call: call.data == 'back', state=main.categories)
async def back_to_main_menu(call: types.CallbackQuery, state: FSMContext):
    buttons = await state.get_data()

    main_menu_btn = InlineKeyboardMarkup(row_width=2)
    main_menu_btn = main_menu_function(main_menu_btn, 2)
    main_menu_btn.row(
        buttons['cart_btn'],
        buttons['all_product_categories_btn']
    )

    main_menu_btn.add(
        buttons['search_btn']
    )

    await call.message.delete()
    await call.message.answer(text='You are at the first page', reply_markup=main_menu_btn)
    # await state.finish()

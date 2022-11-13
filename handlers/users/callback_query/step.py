from loader import db, dp
from states.main import main
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputMedia, input_file
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@dp.callback_query_handler(lambda call: call.data == 'right', state=main.categories)
async def right_callback(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    main_step = db.select_step(id=user_id)[1]
    inner_categories = db.select_all_inner_categories()

    if main_step >= len(inner_categories) - 1:
        await call.answer('Thats all')
    else:
        try:
            main_callback_data = await state.get_data()
            inner_categories_btn = InlineKeyboardMarkup(row_width=2)
            inner_categories = db.select_inner_categories(main_callback_data=main_callback_data['main_categories'])

            img = inner_categories[main_step + 1][0]
            text = inner_categories[main_step + 1][2]

            inner_categories_btn.row(
            InlineKeyboardButton(text='⬅️', callback_data='left'),
            InlineKeyboardButton(text='❌', callback_data='del'),
            InlineKeyboardButton(text='➡️', callback_data='right')
            )
            inner_categories_btn.row(
                InlineKeyboardButton(text='Add to cart 🛒', callback_data='add_to_cart'),
                InlineKeyboardButton(text='About... ✅', callback_data='about')
            )
            inner_categories_btn.add(
                InlineKeyboardButton(text='🔙 Back', callback_data='back')
            )
            file = input_file.InputFile.from_url(url=img)
            await call.message.edit_media(media=InputMedia(media=file, caption=text), reply_markup=inner_categories_btn)
            db.update_step(id=call.from_user.id, step=main_step + 1)
            await state.update_data({
                f"{call.from_user.id}_step": main_step + 1
            })
        except Exception as error:
            print(error)


@dp.callback_query_handler(lambda call: call.data == 'left', state=main.categories)
async def right_callback(call: types.CallbackQuery, state: FSMContext):
    main_step = db.select_step(id=call.from_user.id)[1]
    inner_categories = db.select_all_inner_categories()

    if main_step <= 0:
        await call.answer('Thats all')
    else:
        try:
            await state.update_data({
                'all_products_btn': InlineKeyboardButton(text='All products 📄', callback_data='all_products'),
                'back_btn': InlineKeyboardButton(text='🔙 Back', callback_data='back')
            })
            main_callback_data = await state.get_data()
            inner_categories_btn = InlineKeyboardMarkup(row_width=2)
            inner_categories = db.select_inner_categories(main_callback_data=main_callback_data['main_categories'])

            img = inner_categories[main_step - 1][0]
            text = inner_categories[main_step - 1][2]

            buttons = await state.get_data()
            inner_categories_btn.row(
            InlineKeyboardButton(text='⬅️', callback_data='left'),
            InlineKeyboardButton(text='❌', callback_data='del'),
            InlineKeyboardButton(text='➡️', callback_data='right')
            )
            inner_categories_btn.row(
                InlineKeyboardButton(text='Add to cart 🛒', callback_data='add_to_cart'),
                InlineKeyboardButton(text='About... ✅', callback_data='about')
            )
            inner_categories_btn.add(
                InlineKeyboardButton(text='🔙 Back', callback_data='back')
            )
            file = input_file.InputFile.from_url(url=img)
            await call.message.edit_media(media=InputMedia(media=file, caption=text), reply_markup=inner_categories_btn)
            db.update_step(id=call.from_user.id, step=main_step - 1)
            await state.update_data({
                f"{call.from_user.id}_step": main_step - 1
            })
        except Exception as error:
            print(error)


@dp.callback_query_handler(lambda call: call.data == 'del', state='*')
async def remove_callback_function(call: types.CallbackQuery):
    await call.message.delete()

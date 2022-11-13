from loader import dp, db
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InputFile, InputMedia
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(lambda call: call.data in ['grey', 'gold', 'silver'], state='*')
async def colour_callback(call: types.CallbackQuery, state: FSMContext):
    print(call.data)
    try:
        about = db.select_all_about_product()[0]
        bnts = await state.get_data()
        markup = InlineKeyboardMarkup(row_width=3)
        for i in about[-1].replace(" ", "").split(","):
            markup.insert(
                InlineKeyboardButton(text=i, callback_data=i)
            )
        markup.row(
            InlineKeyboardButton(text='Add to cart 🛒', callback_data='add_to_cart'),
            InlineKeyboardButton(text='Buy ✅', callback_data='buy')
        )
        markup.row(InlineKeyboardButton(text='🔙 Back', callback_data='back'))

        file = InputFile(path_or_bytesio=f'/home/pythonchik/Documents/Telegram_bot/Online_store_bot/images/{call.data}/air/{about[0]}_{call.data}.png')
        await call.message.edit_media(media=InputMedia(media=file, caption=about[2]), reply_markup=markup)
    except Exception as error:
        print(error)

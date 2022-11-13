from loader import dp, db
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InputFile, InputMedia
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(lambda call: call.data == 'about', state='*')
async def about_callback(call: types.CallbackQuery, state: FSMContext):
    about = db.select_all_about_product()[0]
    markup = InlineKeyboardMarkup(row_width=3)
    for i in about[-1].replace(" ", "").split(","):
        markup.insert(
            InlineKeyboardButton(text=i, callback_data=i)
        )
    markup.row(
        InlineKeyboardButton(text='Cart 🛒', callback_data='cart'),
        InlineKeyboardButton(text='Buy ✅', callback_data='buy')
    )
    markup.row(
        InlineKeyboardButton(text='🔙 Back', callback_data='back')
    )

    file = InputFile(path_or_bytesio=f'/home/pythonchik/Documents/Telegram_bot/Online_store_bot/images/grey/air/{about[0]}_grey.png')
    await call.message.edit_media(media=InputMedia(media=file, caption=about[2]), reply_markup=markup)

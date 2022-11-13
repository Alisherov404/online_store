from aiogram import types
from loader import dp
from states.main import main


@dp.callback_query_handler(lambda call: call.data == 'search', state='*')
async def search_callback(call: types.CallbackQuery):
    await call.answer(text='What are you looking for?')
    await call.message.answer('Enter whatever you like')
    await main.search.set()

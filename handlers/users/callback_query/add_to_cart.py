from loader import dp, db
from aiogram import types


@dp.callback_query_handler(lambda call: call.data == 'add_to_cart', state='*')
async def add_to_cart_callback(call: types.CallbackQuery):
    message = call.message
    text = message['caption']
    price = ''
    for item in text.split(" "):
        if item[0] == '$':
            price += item
            break
    try:
        label = db.select_one_cart(id=call.from_user.id, caption=text, price=price)
        print(label)
        if label:
            await call.answer('This item has already been added to cart')
        else:
            db.add_cart(id=call.from_user.id, caption=text, price=price)
    except Exception as error:
        print(error)

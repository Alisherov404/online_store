from aiogram.dispatcher.filters.state import State, StatesGroup


class main(StatesGroup):
    cart =State()
    all_product_categories = State()
    search = State()
    categories = State()

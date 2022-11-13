from aiogram import executor

from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # commands
    await set_default_commands(dispatcher)

    # Create database
    # try:
    #     db.create_table_users()
    # except Exception as err:
    #     print(err)

    # try:
    #     db.create_table_categories()
    # except Exception as err:
    #     print(err)

    # try:
    #     db.create_table_inner_categories()
    # except Exception as err:
    #     print(err)

    # try:
    #     db.create_table_step()
    # except Exception as err:
    #     print(err)

    # try:
    #     db.create_table_cart()
    # except Exception as err:
    #     print(err)

    # try:
    #     db.create_table_about_product()
    # except Exception as err:
    #     print(err)

    # Give information to admin
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)


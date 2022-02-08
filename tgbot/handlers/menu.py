from aiogram import Dispatcher, types

from tgbot.misc.states import load_photo, load_name_adr, load_dom, load_dec, load_price, FSMAdmin, start_photo


async def buy_menu(message: types.Message):
    print(message)


async def sell_menu(message: types.Message):
    await start_photo(message)


def register_menu(dp: Dispatcher):
    dp.register_message_handler(buy_menu, commands=['/Купить_Квартиру?'])
    dp.register_message_handler(sell_menu, commands=['/Продать_Квартиру?'])
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name_adr, state=FSMAdmin.name_adr)
    dp.register_message_handler(load_dom, state=FSMAdmin.dom)
    dp.register_message_handler(load_dec, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)

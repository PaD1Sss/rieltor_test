from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('Купить_Квартиру?')
b2 = KeyboardButton('Продать_Квартиру?')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).add(b2)

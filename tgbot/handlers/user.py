from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.reply import kb_client


async def user_start(message: Message):
    await message.reply(reply_markup=kb_client)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")

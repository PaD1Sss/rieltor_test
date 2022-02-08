from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.reply import kb_client


async def admin_start(message: Message):
    await message.answer(text="Добрый день я БОТ Риэлтор!", reply_markup=kb_client)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)

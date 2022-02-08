
from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

ID = None


class FSMAdmin(StatesGroup):
    photo = State()
    name_adr = State()
    dom = State()
    description = State()
    price = State()


async def start_photo(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply("Загрузить фото!")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply("Введите ваш Адрес: ")


async def load_name_adr(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_adr'] = message.text
        await FSMAdmin.next()
        await message.reply("Введите ваш дом: ")


async def load_dom(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['dom'] = message.text
        await FSMAdmin.next()
        await message.reply("Введите описание: ")


async def load_dec(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
        await FSMAdmin.next()
        await message.reply("Введите цену: ")


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
        await message.answer("Запись добавлена!")
        await state.finish()





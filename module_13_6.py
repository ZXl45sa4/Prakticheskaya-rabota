from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio


api = "7985660415:AAFs9Quf01wTTHZsCuo6xJstXJyt3VkVX4U"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb0 = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Рассчитать', callback_data='Rasschet')
button1 = InlineKeyboardButton(text='Информация', callback_data='Info')
kb0.row(button, button1)
kb = InlineKeyboardMarkup()
button2 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button3 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb.row(button2, button3)
kb1 = InlineKeyboardMarkup()
button4 = InlineKeyboardButton(text='для мужчин', callback_data='men')
button5 = InlineKeyboardButton(text='для женщин', callback_data='women')
kb1.row(button4, button5)


class UserState(StatesGroup):
    age = State()  # возраст
    growth = State()  # рост
    weight = State()  # вес
    age1 = State()  # возраст
    growth1 = State()  # рост
    weight1 = State()  # вес


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb0)


@dp.callback_query_handler(text='Rasschet')
async def get_formulas(call):
    await call.message.answer('Выберите опцию:', reply_markup=kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer("для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5 \n"
                              "для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161 \n")


@dp.callback_query_handler(text='calories')
async def get_formulas(call):
    await call.message.answer('Выберите опцию:', reply_markup=kb1, )


@dp.callback_query_handler(text='men')
async def set_age(call):
    await call.message.answer('Введите свой возраст(г):')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)  # аргумент пример first  можно называть как угодно
    data = await state.get_data()
    await message.answer('Введите свой рост(см):')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    data = await state.get_data()
    await message.answer('Введите свой вес(кг):')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    F = (10 * float(data['weight'])) + (6.25 * float(data['growth'])) - (
            5 * float(data['age'])) + 5
    await message.answer(f"Ваша норма: {F} калорий")
    await state.finish()

@dp.callback_query_handler(text='women')
async def set_age1(call):
    await call.message.answer('Введите свой возраст(г):')
    await UserState.age1.set()


@dp.message_handler(state=UserState.age1)
async def set_growth1(message, state):
    await state.update_data(age1=message.text)  # аргумент пример first  можно называть как угодно
    data = await state.get_data()
    await message.answer('Введите свой рост(см):')
    await UserState.growth1.set()


@dp.message_handler(state=UserState.growth1)
async def set_weight1(message, state):
    await state.update_data(growth1=message.text)
    data = await state.get_data()
    await message.answer('Введите свой вес(кг):')
    await UserState.weight1.set()


@dp.message_handler(state=UserState.weight1)
async def send_calories(message, state):
    await state.update_data(weight1=message.text)
    data = await state.get_data()
    F1 = (10 * float(data['weight1'])) + (6.25 * float(data['growth1'])) - (
                5 * float(data['age1'])) - 161
    await message.answer(f"Ваша норма: {F1} калорий")
    await state.finish()


@dp.message_handler()
async def all_massages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
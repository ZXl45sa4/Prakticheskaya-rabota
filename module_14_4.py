from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

import crud_functions
from crud_functions import *

api = "7985660415:AAFs9Quf01wTTHZsCuo6xJstXJyt3VkVX4U"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb0 = ReplyKeyboardMarkup(resize_keyboard=True,
                          keyboard=[
                              [
                                  KeyboardButton(text='Рассчитать'),
                                  KeyboardButton(text='Информация')
                              ],
                              [KeyboardButton(text='Купить')]
                          ]
                          )
catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=f"Product1", callback_data="product_buying"),
            InlineKeyboardButton(text=f"Product2", callback_data="product_buying"),
            InlineKeyboardButton(text=f"Product3", callback_data="product_buying"),
            InlineKeyboardButton(text=f"Product4", callback_data="product_buying")
        ]
    ]
)

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


@dp.message_handler(text='Рассчитать')
async def get_formulas(message):
    await message.answer('Выберите опцию:', reply_markup=kb)


@dp.message_handler(text='Информация')
async def get_formulas(message):
    await message.answer("для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5 \n"
                         "для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161 \n")


@dp.message_handler(text='Купить')
async def get_all_products(message):

    with open('files/1.jpg', "rb") as img1:
        await message.answer_photo(img1, crud_functions.tovar[0])
    with open('files/2.jpg', "rb") as img2:
        await message.answer_photo(img2, crud_functions.tovar[1])
    with open('files/3.jpg', "rb") as img3:
        await message.answer_photo(img3, crud_functions.tovar[2]),
    with open('files/4.jpg', "rb") as img4:
        await message.answer_photo(img4, crud_functions.tovar[3]),
    await message.answer('Выберете продукт для покупки:', reply_markup=catalog_kb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")


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

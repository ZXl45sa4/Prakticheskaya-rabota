from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()  # возраст
    growth = State()  # рост
    weight = State()  # вес


@dp.message_handler(text='Calories')
async def set_age(message):
    await message.answer('Введите свой возраст(г):')
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
    F = (float(10) * float(data['weight'])) + (float(6.25) * float(data['growth'])) - (
                float(5) * float(data['age'])) + 5
    await message.answer(f"Ваша норма: {F} калорий")
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

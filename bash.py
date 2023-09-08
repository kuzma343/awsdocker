import logging
import subprocess
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Кнопки, які буде натискати користувач
start_button = types.KeyboardButton('Запустити скрипт')
button1 = types.KeyboardButton('запустити контейнер')
button2 = types.KeyboardButton('зупинити контейнер')
button3 = types.KeyboardButton('видалити контейнер')
button4 = types.KeyboardButton('оновити контейнер')

# Розмітка з кнопками
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(start_button)
markup.add(button1, button2)
markup.add(button3, button4)

@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await message.reply("Привіт! Обери, який скрипт запустити.", reply_markup=markup)

@dp.message_handler(lambda message: message.text == "Запустити скрипт")
async def run_script(message: types.Message):
    try:
        subprocess.run(['/awsdocker/qwerty.sh'], check=True, shell=True)
        await message.reply("Скрипт успішно запущений!")
    except subprocess.CalledProcessError:
        await message.reply("Під час виконання скрипту сталася помилка.")

@dp.message_handler(lambda message: message.text == "запустити контейнер")
async def run_script_1(message: types.Message):
    try:
        subprocess.run(['/awsdocker/qwerty2.sh'], check=True, shell=True)
        await message.reply("Скрипт успішно запущений!")
    except subprocess.CalledProcessError:
        await message.reply("Під час виконання скрипту сталася помилка.")

@dp.message_handler(lambda message: message.text == "зупинити контейнер")
async def run_script_2(message: types.Message):
    try:
        subprocess.run(['/awsdocker/qwerty3.sh'], check=True, shell=True)
        await message.reply("Скрипт успішно запущений!")
    except subprocess.CalledProcessError:
        await message.reply("Під час виконання скрипту сталася помилка.")

@dp.message_handler(lambda message: message.text == "видалити контейнер")
async def run_script_3(message: types.Message):
    try:
        subprocess.run(['/awsdocker/qwerty4.sh'], check=True, shell=True)
        await message.reply("Скрипт успішно запущений!")
    except subprocess.CalledProcessError:
        await message.reply("Під час виконання скрипту сталася помилка.")

@dp.message_handler(lambda message: message.text == "оновити контейнер")
async def run_script_4(message: types.Message):
    try:
        subprocess.run(['/awsdocker/qwerty5.sh'], check=True, shell=True)
        await message.reply("Скрипт успішно запущений!")
    except subprocess.CalledProcessError:
        await message.reply("Під час виконання скрипту сталася помилка.")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)


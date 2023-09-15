import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.utils import executor
import subprocess
API_TOKEN = '6635168570:AAF_Gh6YdoT1Cv6MWxfBXggOZhEsOy9uuIE'  # Підставте свій API токен
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

password = 'password'  # Підставте свій пароль тут

global i  # Додаємо цей рядок для позначення того, що i - глобальна змінна

authenticated = False  # Змінна для відстеження стану автентифікації

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    global i, authenticated
    if not authenticated:
        await message.reply("Введіть пароль:")
    else:
        await message.reply("Привіт! Обери, який скрипт запустити.", reply_markup=markup)

@dp.message_handler(lambda message: message.text == password)
async def process_password_correct(message: types.Message):
    global i, authenticated
    authenticated = True  # Користувач автентифікований
    await message.reply("Пароль вірний. Ласкаво просимо!")
    i = 1

@dp.message_handler(lambda message: message.text != password)
async def process_password_incorrect(message: types.Message):
    await message.reply("Пароль невірний. Спробуйте ще раз:")


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
@dp.message_handler(lambda message: message.text == "Запустити скрипт")
async def run_script(message: types.Message):
    try:
        subprocess.run(['/awsdocker/qwerty.sh'], check=True, shell=True)
        await message.reply("Скрипт успішно запущений!")
    except subprocess.CalledProcessError:
        await message.reply("Під час виконання скрипту сталася помилка.")
# Обробник для кнопки
@dp.message_handler(lambda message: message.text == "запустити контейнер")
async def run_script_1(message: types.Message):
    try:
        subprocess.run(['/awsdocker/qwerty2.sh'], check=True, shell=True)
        await message.reply("Скрипт успішно запущений!")
    except subprocess.CalledProcessError:
        await message.reply("Під час виконання скрипту сталася помилка.")
# Обробник для кнопки
@dp.message_handler(lambda message: message.text == "зупинити контейнер")
async def run_script_2(message: types.Message):
    try:
        subprocess.run(['/awsdocker/qwerty3.sh'], check=True, shell=True)
        await message.reply("Скрипт успішно запущений!")
    except subprocess.CalledProcessError:
        await message.reply("Під час виконання скрипту сталася помилка.")
# Обробник для кнопки
@dp.message_handler(lambda message: message.text == "видалити контейнер")
async def run_script_3(message: types.Message):
    try:
        subprocess.run(['/awsdocker/qwerty4.sh'], check=True, shell=True)
        await message.reply("Скрипт успішно запущений!")
    except subprocess.CalledProcessError:
        await message.reply("Під час виконання скрипту сталася помилка.")
# Обробник для кнопки
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


i=0


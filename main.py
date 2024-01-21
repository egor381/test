from gigachat import GigaChat
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = "6902051695:AAE8K_DmzZNJjoWIHc8nH0Xr0-US2uW40Gw"

bot = Bot(token)
dp = Dispatcher(bot)

# giga = GigaChat(
#     credentials='NzIwYjRmYzEtNDkyYi00NzFjLWE4ODAtYzM4OWVhYTI4M2M2OmYwMGI4MzFiLWZmNDgtNGNmOS04ZjE5LTFjYTA1NjM5ODJhNw==',
#     verify_ssl_certs=False
# )

users = {275673431, 75624, 6325574999}
accepted_users = lambda message: message.from_user.id not in users


@dp.message_handler(accepted_users, content_types=['any'])
async def handle_unwanted_users(message: types.Message):
    await message.answer('Извините, бот работает только для VIP пользователей 😎')
    return


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Привет, и тебя зовут " + message.from_user.full_name + "\nИ твой id: " + str(message.from_user.id))


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет, на связи Chat Gpt, я думаю ты знаешь, что это такое. Можешь мне задать любой вопрос")


@dp.message_handler()
async def send(message: types.Message):
    await message.answer('⏳Обрабатываю запрос')
    # response = giga.chat(message.text)
    # await message.answer(response.choices[0].message.content)


def on_startup_bot():
    print("Bot started")


executor.start_polling(dp, skip_updates=True, on_startup=on_startup_bot, timeout = 1)

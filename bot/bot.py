import logging
import messages
import api_service

from config import BOT_API_TOKEN
from aiogram import Bot, Dispatcher, executor, types


#  Token
API_TOKEM = BOT_API_TOKEN

#  Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEM)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'products'])
async def send_welcome(message: types.Message):
    await message.reply(text=messages.welcome())
    await send_products(message=message.products())



@dp.message_handler(commands=['products'])
async def send_products(message: types.Message):
    page = int(message)
    await message.answer(text=messages.products(page))


@dp.message_handler(commands=['product'])
async def send_product(message: types.Message):
    product_id = int(message)
    await message.answer(text=messages.product(product_id))


@dp.message_handler(commands=['category'])
async def send_category(message: types.Message):
    category = message
    await message.answer(text=messages.category(category))


@dp.message_handler(commands=['categories'])
async def send_catrgories(message: types.Message):
    page = int(message)
    await message.answer(text=messages.categories(page))


@dp.message_handler(commands=['add_to_cart'])
async def add_to_cart(message: types.Message):
    product = int(message)
    await message.answer(text=messages.add_to_cart(product))


@dp.message_handler(commands=['del_from_cart'])
async def del_from_cart(message: types.Message):
    product = int(message)
    await message.answer(text=messages.del_from_cart(product))


@dp.message_handler(commands=['cart'])
async def send_cart(message: types.Message):
    user_id = int(message)
    await message.answer(text=messages.cart(user_id))


@dp.message_handler(commands=['make_order'])
async def make_order(message: types.Message):
    user_id = int(message)
    await message.answer(text=messages.make_order(user_id))


@dp.message_handler(commands=['orders'])
async def send_orders(message: types.Message):
    user_id = int(message)
    await message.answer(text=messages.get_orders(user_id))



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

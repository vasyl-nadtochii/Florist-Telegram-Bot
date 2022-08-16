from email.message import Message
import logging

import Config.config as config
import Config.debug_helper as helper

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig (level = logging.INFO)

bot= Bot(token= config.TOKEN)
dp= Dispatcher(bot, storage = MemoryStorage())

@dp.message_handler(commands = ['start'])
async def on_start(message: Message):
    await message.answer("Hello world, this is the first line of Florist bot)")

# TODO: temporary - remove that later
@dp.message_handler()
async def echo(message: Message):
    text = f"You entered: {message.text}"
    await bot.send_message(chat_id=message.from_user.id, text = text)

if __name__ == '__main__':
    executor.start_polling(
        dp, 
        skip_updates = True, 
        on_startup = helper.on_bot_started()
    )
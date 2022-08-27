from email.message import Message

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import Config.config as config
import Config.debug_helper as helper
import logging

from Florist.Services.Localizables.localizables import LocalizableManager
from Florist.Resources.Keyboards.keyboards import KeyboardMananger

logging.basicConfig (level = logging.INFO)

bot = Bot(token= config.TOKEN)
dp = Dispatcher(bot, storage = MemoryStorage())

localized_manager = LocalizableManager()
keyboard_manager = KeyboardMananger()

@dp.message_handler(commands = ['start'])
async def on_start(message: Message):
    await message.reply(
        localized_manager.get_localized_string(key = "intro_message"),
        reply_markup = keyboard_manager.get_start_keyboard()
    )

# TODO: temporary - remove that later
@dp.message_handler()
async def echo(message: Message):
    text = f"You entered: {message.text}"
    await bot.send_message(chat_id = message.from_user.id, text = text)

if __name__ == '__main__':
    executor.start_polling(
        dp, 
        skip_updates = True, 
        on_startup = helper.on_bot_started()
    )
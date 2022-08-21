from email.message import Message

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

import Config.config as config
import Config.debug_helper as helper
import logging

from Florist.Services.Localizables.localizables import LocalizableManager

logging.basicConfig (level = logging.INFO)

bot = Bot(token= config.TOKEN)
dp = Dispatcher(bot, storage = MemoryStorage())

localized_manager = LocalizableManager()

@dp.message_handler(commands = ['start'])
async def on_start(message: Message):
    sign_in_btn = KeyboardButton(localized_manager.get_localized_string("sign_in_btn_text"))
    sign_up_btn = KeyboardButton(localized_manager.get_localized_string("sign_up_btn_text"))

    keyboard = ReplyKeyboardMarkup(
        resize_keyboard = True,
         one_time_keyboard = True
    ).add(
        sign_in_btn
    ).add(
        sign_up_btn
    )

    await message.reply(
        localized_manager.get_localized_string(key = "intro_message"),
         reply_markup = keyboard
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
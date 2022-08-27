import logging

from aiogram.types import Message
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import Config.config as config
import Config.debug_helper as helper
from Config.debug_helper import Logger

from Florist.Services.Localizables.localizables import LocalizableManager
from Florist.Resources.Keyboards.keyboards import KeyboardManager

from Florist.StatesGroups.Start import start_states

logging.basicConfig (level = logging.INFO)

bot = Bot(token= config.TOKEN)
dp = Dispatcher(bot, storage = MemoryStorage())

localized_manager = LocalizableManager()
keyboard_manager = KeyboardManager()

if __name__ == '__main__':
    start_states.setup(dp)
    executor.start_polling(
        dp, 
        skip_updates = True, 
        on_startup = helper.on_bot_started()
    )
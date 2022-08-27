from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher
from aiogram.types import Message

from bot import keyboard_manager, localized_manager

from Config.debug_helper import Logger

class StartStates(StatesGroup):
    request_auth = State()

async def on_start(message: Message):
    await message.answer(
        localized_manager.get_localized_string(key = "intro_message"),
        reply_markup = keyboard_manager.get_start_keyboard()
    )
    await StartStates.request_auth.set()

async def proceed_chosen_auth_method(message: Message):
    if message.text == localized_manager.get_localized_string(key = "sign_in_btn_text"):
        # TODO: implement in future
        pass
    elif message.text == localized_manager.get_localized_string(key = "sign_up_btn_text"):
        await message.answer(
            localized_manager.get_localized_string(key = "sign_up_started"),
            reply_markup = keyboard_manager.remove_reply_keyboard()
        )
        await message.answer(localized_manager.get_localized_string(key = "sign_up_request_phone_message"))

def setup(dp: Dispatcher):
    dp.register_message_handler(on_start, commands = ['start'])
    dp.register_message_handler(proceed_chosen_auth_method, state = StartStates.request_auth)
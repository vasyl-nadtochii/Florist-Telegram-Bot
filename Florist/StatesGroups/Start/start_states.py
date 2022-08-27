from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher
from aiogram.types import Message

from bot import keyboard_manager, localized_manager, dp

class StartStates(StatesGroup):
    request_auth = State()

async def on_start(message: Message):
    await message.reply(
        localized_manager.get_localized_string(key = "intro_message"),
        reply_markup = keyboard_manager.get_start_keyboard()
    )

# TODO: temporary - remove that later
async def echo(message: Message):
    text = f"You entered: { message.text }"
    await message.answer(
        text = text,
        reply_markup = keyboard_manager.remove_reply_keyboard()
    )

def setup(dp: Dispatcher):
    dp.register_message_handler(on_start, commands = ['start'])
    dp.register_message_handler(echo)
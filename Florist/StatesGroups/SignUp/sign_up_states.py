from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message

class SignUpStates(StatesGroup):
    request_phone_state = State()
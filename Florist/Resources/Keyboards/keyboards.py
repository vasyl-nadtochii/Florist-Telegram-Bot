from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from Florist.Services.Localizables.localizables import LocalizableManager

class KeyboardManager:

    def __init__(self):
        self.localized_manager = LocalizableManager()

    def remove_reply_keyboard(self):
        return ReplyKeyboardRemove()

    def get_start_keyboard(self):
        sign_in_btn = KeyboardButton(self.localized_manager.get_localized_string("sign_in_btn_text"))
        sign_up_btn = KeyboardButton(self.localized_manager.get_localized_string("sign_up_btn_text"))

        return ReplyKeyboardMarkup(
            resize_keyboard = True,
            one_time_keyboard = True
        ).add(
            sign_in_btn
        ).add(
            sign_up_btn
        )
from datetime import datetime

from colorama import Fore
from colorama import Style

from enum import Enum

class Logger:
    class MessageType(Enum):
        info = "INFO:"
        debug = "DEBUG:"
        error = "ERROR:"
        warning = "WARNING:"
        common = str()

    @staticmethod
    def log(message: str, type: MessageType = MessageType.common):
        if type == Logger.MessageType.common:
            print(message)
        else:
            color = None
            if type == Logger.MessageType.info:
                color = Fore.GREEN
            elif type == Logger.MessageType.debug:
                color = Fore.MAGENTA
            elif type == Logger.MessageType.error:
                color = Fore.RED
            elif type == Logger.MessageType.warning:
                color = Fore.YELLOW

            print(f"{ color }{ type.value } { message }{ Style.RESET_ALL }")

def on_bot_started():
    time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    Logger.log(f"Bot started successfully at { time }", Logger.MessageType.info)
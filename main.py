import os
from Config.debug_helper import Logger

def __clear_console():
    if os.name == 'nt': # for windows
      _ = os.system('cls')
    else: # for mac and linux
        os.system('clear')

__clear_console()

def __start():
    choice = None

    Logger.log("Choose what to run from options below:", Logger.MessageType.info)
    Logger.log("1 - Run Florist Bot")
    Logger.log("2 - Run Florist Bot Unit Tests")

    try:
        choice = int(input("Your choice: "))
    except:
        __clear_console()
        Logger.log("Wrong input type, try again", Logger.MessageType.error)
        __start()
        return

    __clear_console()
    if choice == 1:
        os.system('python bot.py')
    elif choice == 2:
        os.system('python tests.py')
    else:
        Logger.log("Wrong option, try again", Logger.MessageType.error)
        __start()

try:
    __start()
except KeyboardInterrupt:
    Logger.log("You've terminated code execution via keyboard interruption!", Logger.MessageType.debug)
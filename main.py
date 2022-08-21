import os
from secrets import choice

def __start():
    def request_choice():
        try:
            choice = int(input("Your choice: "))
        except:
            print("ERROR: Wrong input type, try again")
            request_choice()

        return choice

    print("MAIN: Choose what to run from options below:")
    print("1 - Run Florist Bot")
    print("2 - Run Florist Bot Unit Tests")

    option = request_choice()

    if option == 1:
        os.system('python bot.py')
    elif option == 2:
        os.system('python tests.py')
    else:
        print("Wrong option, try again")
        __start()

try:
    __start()
except KeyboardInterrupt:
    print("INFO: You've terminated code execution via keyboard interruption!")
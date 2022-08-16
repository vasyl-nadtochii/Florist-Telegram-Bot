import json

class LocalizableManager:

    __localizable = {}

    def __init__(self):
        with open("Resources\Localizables\localizables_eng.json", encoding = "utf-8") as json_file:
            self.__localizable = json.load(json_file)
            

    def get_localized_string(self, key):
        try:
            return self.__localizable[key]
        except:
            return key

        
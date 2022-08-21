import json

class LocalizableManager:

    __localizable = {}

    def __init__(self):
        with open("Florist\Resources\Localizables\localizables_eng.json", encoding = "utf-8") as json_file:
            self.__localizable = json.load(json_file)
            

    def get_localized_string(self, key):
        if not isinstance(key, str):
            return None
        try:
            return self.__localizable[key]
        except:
            return key
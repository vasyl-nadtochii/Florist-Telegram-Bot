from unittest import TestCase
from Florist.Services.Localizables.localizables import LocalizableManager

class LocalizableManagerTests(TestCase):

    def test_correct_key_value(self):
        sut = LocalizableManager()
        self.assertEqual(sut.get_localized_string(key = "test_key"), "Test Value")

    def test_wrong_key_value(self):
        sut = LocalizableManager()
        self.assertEqual(sut.get_localized_string(key = "test_wrong_key"), "test_wrong_key")

    def test_wrong_key_type(self):
        class SomeDummyClass:
            pass
    
        sut = LocalizableManager()
        self.assertEqual(sut.get_localized_string(key = SomeDummyClass()), None)

        sut = LocalizableManager()
        self.assertEqual(sut.get_localized_string(key = 23213), None)
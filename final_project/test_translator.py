import unittest
from machinetranslation.translator import french_to_english, english_to_french

class TestTranslatorMethods(unittest.TestCase):

    def test_f_to_e(self):
        text = "Bonjour, comment vous êtes aujourd'hui?"
        translation = 'Hello, how are you today?'
        response = french_to_english(text)
        self.assertEqual(response["translations"][0]["translation"], translation)
        self.assertNotEqual(response["translations"][0]["translation"], text)
    
    def test_e_to_f(self):
        text = 'Hello, how are you today?'
        translation = "Bonjour, comment vous êtes aujourd'hui?"
        response = english_to_french(text)
        self.assertEqual(response["translations"][0]["translation"], translation)
        self.assertNotEqual(response["translations"][0]["translation"], text)

if __name__ == '__main__':
    unittest.main()

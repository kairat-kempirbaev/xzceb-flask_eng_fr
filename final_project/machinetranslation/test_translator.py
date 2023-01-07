import unittest
from translator import french_to_english, english_to_french


class TestTranslatorMethods(unittest.TestCase):

    def test_f_to_e_empty_input(self):
        with self.assertRaises(Exception) as context:
            french_to_english("")
        self.assertTrue('Wrong input' in str(context.exception))

    def test_f_to_e_null_input(self):
        with self.assertRaises(Exception) as context:
            french_to_english(None)
        self.assertTrue('Wrong input' in str(context.exception))

    def test_f_to_e(self):
        text = "Bonjour, comment vous êtes aujourd'hui?"
        translation = 'Hello, how are you today?'
        response = french_to_english(text)
        self.assertEqual(response, translation)
        self.assertNotEqual(response, text)

    def test_e_to_f_empty_input(self):
        with self.assertRaises(Exception) as context:
            english_to_french("")
        self.assertTrue('Wrong input' in str(context.exception))

    def test_e_to_f_null_input(self):
        with self.assertRaises(Exception) as context:
            english_to_french(None)
        self.assertTrue('Wrong input' in str(context.exception))

    def test_e_to_f(self):
        text = 'Hello, how are you today?'
        translation = "Bonjour, comment vous êtes aujourd'hui?"
        response = english_to_french(text)
        self.assertEqual(response, translation)
        self.assertNotEqual(response, text)


if __name__ == '__main__':
    unittest.main()

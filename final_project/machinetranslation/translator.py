'''Module will use IBM watson service to make bidirectional english-french translation'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ['apikey']
URL = os.environ['url']
VERSION = "2022-11-29"
authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)
language_translator.set_service_url(URL)

EN_TO_FR_FORMAT = "en-fr"
FR_TO_EN_FORMAT = "fr-en"

def english_to_french(english_text):
    '''Translate english to french, only text'''

    if None is english_text or 0 is len(english_text) :
        raise ValueError('Wrong input')

    ibm_translation = language_translator.translate(
        text=english_text,
        model_id=EN_TO_FR_FORMAT).get_result()
    return ibm_translation["translations"][0]["translation"]


def french_to_english(french_text):
    '''Translate  french to english, only text'''
    if None is french_text or 0 is len(french_text) :
        raise ValueError('Wrong input')

    ibm_translation = language_translator.translate(
        text=french_text,
        model_id=FR_TO_EN_FORMAT).get_result()
    return ibm_translation["translations"][0]["translation"]

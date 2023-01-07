import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
version = "2022-11-29"
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)
language_translator.set_service_url(url)


def english_to_french(englishText):
    en_to_fr_format = "en-fr"
    ibm_translation = language_translator.translate(
        text=englishText,
        model_id=en_to_fr_format).get_result()
    return ibm_translation["translations"][0]["translation"]


def french_to_english(frenchText):
    fr_to_en_format = "fr-en"
    ibm_translation = language_translator.translate(
        text=frenchText,
        model_id=fr_to_en_format).get_result()
    return ibm_translation["translations"][0]["translation"]

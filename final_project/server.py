from machinetranslation import english_to_french, french_to_english
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return json.dumps(english_to_french(textToTranslate), indent=2, ensure_ascii=False)


@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return json.dumps(french_to_english(textToTranslate), indent=2, ensure_ascii=False)


@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

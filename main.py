from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    translation = None
    if request.method == "POST":
        text_to_translate = request.form["text_to_translate"]
        if text_to_translate.strip():  # Check if the input is not empty
            translator = Translator()
            translated_text = translator.translate(text_to_translate, src='en', dest='hi')
            translation = translated_text.text
        else:
            translation = "No text provided for translation."  # Handle empty input
    return render_template("index.html", translation=translation)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask,render_template,request
import torch
from seamless_communication.models.inference import Translator

app = Flask(__name__)
 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_language = request.form.get('disabledSelect')
        audio_file = request.files.get('fileInput')

        if audio_file and selected_language:
            translated_text = translate_audio(audio_file, selected_language)
            return render_template('home.html', translation=translated_text)

    return render_template('home.html', translation=None)

def translate_audio(audio_file, target_language):
    translated_text = f'Translated text in {target_language}'
    return translated_text



if __name__ == '__main__':
    app.run(debug=True)
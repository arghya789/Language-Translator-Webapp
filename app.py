import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from flask import Flask , render_template, request, url_for
app = Flask(__name__)

@app.route('/')

def index():
    return 'Index Page'

@app.route('/hello')

def hello():
    return 'Hello, World'

@app.route('/translate', methods=['GET'])

def translate():
    lang=request.form['languages']
    lang=lang.lower()
    if(lang=="kannada"):
        dest_code='kn'
    if(lang=="japanese"):
        dest_code='ja'
    if(lang=="hindi"):
        dest_code='hi'
    if(lang=="telugu"):
        dest_code='te'   
    if(lang=="tamil"):
        dest_code='ta'

    
    translator=Translator()
    recog1=sr.Recognizer()
    mc=sr.Microphone()
    with mc as source:
        print("Say phrase to be translated.....")
        recog1.adjust_for_ambient_noise(source, duration=0.3)
        sent=recog1.listen(source)
        sentence=recog1.recognize_google(sent)
        print("You said: "+sentence)
        text_to=translator.translate(sentence,dest=lang)
        text=text_to.text
        print(text)
        speak=gTTS(text=text, lang=lang, slow=False)
    return render_template('index.html', prediction=text)

if __name__ == '__main__':
	app.run(debug=True)
     

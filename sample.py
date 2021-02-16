import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import pyttsx3
engine = pyttsx3.init()

translator=Translator()

recog1 = sr.Recognizer()
mc=sr.Microphone()
with mc as source:
    print("Say hello...")
    recog1.adjust_for_ambient_noise(source,duration=0.3)
    print("listening")
    audio=recog1.listen(source)
    text=recog1.recognize_google(audio)
    print(text)

if 'hello' in text:
    try:
        print("say source language")
        with mc as source:
            recog1.adjust_for_ambient_noise(source, duration=0.3)
            lang1=recog1.listen(source)
            fromlang=recog1.recognize_google(lang1)
            print("from language is "+fromlang)
            if fromlang=="English":
                fromlang='en'
            print("say destination language")
            recog1.adjust_for_ambient_noise(source, duration=0.3)
            lang2=recog1.listen(source)
            tolang=recog1.recognize_google(lang2)
            print("to language is "+tolang)
            if tolang=="Hindi":
                tolang='hi'
            print("say phrase to be translated")
            recog1.adjust_for_ambient_noise(source, duration=0.3)
            sent=recog1.listen(source)
            sentence=recog1.recognize_google(sent)
            print("You said: "+sentence)
            text_to=translator.translate(sentence,src=fromlang,dest=tolang)
            text=text_to.text
            print(text)
            engine.say(text)
            speak=gTTS(text=text, lang=tolang, slow=False)
        
    except sr.UnknownValueError:
        print("Unable to understand the input")
    except sr.RequestError as e:
        print("Unable to provide Required output".format(e))

        

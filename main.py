import speech_recognition as sr
import webbrowser
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            nova_speech(ask)
        audio = r.listen(source)
        voice_data = ''

        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            nova_speech("Sorry,I did not get that")
        except sr.RequestError:
            nova_speech("Sorry,My sppech service is down")

        return voice_data

def nova_speech(audio_string):
    tts = gTTS(text=audio_string,lang='en')
    r = random.randint(1,10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if('hey Nova') in voice_data:
        nova_speech("Hello, How can i help Today")
    if ('what is your name') in voice_data:
        nova_speech("My name is nova")
    if ('what time is it') in voice_data:
        nova_speech(ctime())
    if ('search') in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        nova_speech("Here is what I found for "+search)
    if('location') in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location 
        webbrowser.get().open(url)
        nova_speech("I found "+location)
    if('play song') in voice_data:
        song = record_audio('What is the song?')
        url = 'https://www.youtube.com/results?search_query=' + song 
        webbrowser.get().open(url)
        nova_speech("I found "+ song)
    if ('exit' in voice_data):
        print("Have a nice day")
        exit()


nova_speech("How Can I help you?")
while True:
    voice_data = record_audio()
    respond(voice_data)
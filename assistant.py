import speech_recognition as sr
from  time import ctime
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
r = sr.Recognizer()

def record_audio(ask=False):
    
    with  sr.Microphone()as source:
        if ask:
            dasu_speak(ask)
        audio =r.listen(source)
        voice_data=''
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            dasu_speak('Sorry , I am not able to hear')
        except sr.RequestError:
            dasu_speak("Sorry , I am low at service")
        return voice_data    

def dasu_speak(audio_string):
    tts=gTTS(text=audio_string,lang='en')
    r=random.randint(1,10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    
    
def respond(voice_data):
    if "kya naam hai tumhara" in voice_data:
        dasu_speak("My name is Dasu")
    if "what is your name"in voice_data:
        dasu_speak("My name is Dasu")
    if "what time it is" in voice_data:
        dasu_speak(ctime())
    if "search"in voice_data:
        search = record_audio("Kya Search Marna Hai?")
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        dasu_speak("Yeh Dekho muje Yeh Mila " +search)
    if "location"in voice_data:
        location = record_audio("What is the location ")
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        dasu_speak("Yeh Raha aapka Location " + location)
    if "exit"in voice_data:
        exit()
        
time.sleep(1)
dasu_speak("How can I Help you?")
while 1:
    voice_data = record_audio()
    respond(voice_data)
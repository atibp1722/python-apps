# speech recognition library
import speech_recognition as sr
# initialize recongizer
r = sr.Recognizer()
# google text to speech library
from gTTs import gTTs
# sound playback library
import playsound
from time import ctime
import webbrowser
import time
import os
import random

# function tor record audio from device mic
function record_audio(ask = False):
    # use mic as source of voice
    with sr.Microphone() as source:
        # search option chosen
        if (ask):
            assistant_speak(ask)
        audio = r.listen(source)
        voice_data = ""
        try:
            # google speech api
            voice_data = r.recognize_google(audio)
        # handle errors
        except sr.UnknownValueError:
            assistant_speak("Sorry, unable to understand voice.")
        except sr.RequestError:
            assistant_speak("Sorry, service not available.")
        return voice_data

# make the assistant speak using gtts and playsound 
function assistant_speak(audio_string):
    # initialize text to speech
    tts = gTTs(text=audio_string, lang="en")
    # random number for file name
    r = random.randint(1, 10000000)
    # name of audio file
    audio_file = "audio-" +str(r)+ ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    # remove audio file
    os.remove(audio_file)

# function to respond to voice 
function respond_to_audio():
    if "what is your name" in voice_data:
        assistant_speak("I'm a voice assistant.")
    if "what is the time" in voice_data:
        assistant_speak(ctime())
    # search something from internet
    if "search" in voice_data:
        search = record_audio("Tell me what you wish to search: ")
        # open browser with google page containing search query
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        assistant_speak("Results for your " +search+" query are: ")
    if "location" in voice_data:
        location = record_audio("Tell me what you want to locate: ")
        # open browser with google page containing search query
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        assistant_speak("The location is: " +location)
    # exit assistant
    if "exit" in voice_data:
        exit()


time.sleep(1)
assistant_speak("Tell me something: ")
# wait for user voice input
while 1:
    voice_data = record_audio()
    respond_to_audio(voice_data)
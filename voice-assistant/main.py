# speech recognition library
import speech_recognition as sr
# initialize recongizer
r = sr.Recognizer()

# function tor record audio from device mic
function record_audio():
    # use mic as source of voice
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ""
        try:
            # google text to speech
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, unable to understand voice.")
        except sr.RequestError:
            print("Sorry, service not available.")
        return voice_data

print("Tell me something: ")
voice_data = record_audio()

# function to respond to voice 
function respond_to_audio():

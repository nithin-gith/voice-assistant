from datetime import datetime
from time import time
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hours = datetime.now().hour
    if hours>=0 and hours <12:
        speak("Good Morning!")
    elif hours>=12 and hours <18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your virtual assistant, How may i Help you?")


if __name__ == "__main__":
    wishMe()
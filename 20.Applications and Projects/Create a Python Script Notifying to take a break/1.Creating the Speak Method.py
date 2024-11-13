import pyttsx3
from plyer import notification
import time


# Speak method
def Speak(self, audio):
    # Calling the intial constructor
    # of pyttsx3
    engine = pyttsx3.init('sapi5')

    # Calling the getter method
    voices = engine.getProperty('voices')

    # Calling the setter method
    engine.setProperty('voice', voices[1].id)

    engine.say(audio)
    engine.runAndWait()

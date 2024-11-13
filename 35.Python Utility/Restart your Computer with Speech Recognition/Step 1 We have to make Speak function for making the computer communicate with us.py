# Method to give
# output voice commands
def Speak(self, audio):
    engine = pyttsx3.init('sapi5')

    # intial constructor of pyttsx3
    voices = engine.getProperty('voices')

    # getter and setter method
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

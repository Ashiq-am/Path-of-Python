# Method for voice output
def Speak(self, audio):
    # Constructor call for pyttsx3.init()
    engine = pyttsx3.init('sapi5')

    # Setting voice type and id
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

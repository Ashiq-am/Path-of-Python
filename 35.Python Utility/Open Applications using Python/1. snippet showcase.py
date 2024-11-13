# create object
engine = pyttsx3.init()

# assign voice
voices = engine.getProperty('voices')

#changing index changes voices but ony 0 and 1 are working here
engine.setProperty('voice', voices[1].id)

# run tool
engine.runAndWait()

print("")

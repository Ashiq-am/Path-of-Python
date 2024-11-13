try:
    command = voice.recognize_google(voice_command)

# handle the exceptions
except speech.UnknownValueError:
    print("Google Speech Recognition system could not understand your \
    instructions please give instructions carefully")

except speech.RequestError as e:
    print("Could not request results from Google Speech Recognition\
    service; {0}".format(e))

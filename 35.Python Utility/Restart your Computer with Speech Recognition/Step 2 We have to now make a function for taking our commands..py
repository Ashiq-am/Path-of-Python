# Method to take
# input voice commands
def take_commands(self):
    r = sr.Recognizer()

    # Making the use of Recognizer
    # and Microphone method from
    # Speech Recognition for taking commands
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        # seconds of non-speaking audio
        # before a phrase is considered complete
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')

            # For listening the command in indian english
            print("the query is printed='", Query, "'")

        # For printing the query or the
        # command that we give
        except Exception as e:

            # This is for printing the exception
            print(e)
            print("Say that again sir")
            return "None"
    return Query

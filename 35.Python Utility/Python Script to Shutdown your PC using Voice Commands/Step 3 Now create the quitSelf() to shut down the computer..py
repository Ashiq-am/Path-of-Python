# Method to self shut down system
def quitSelf(self):
    self.Speak("do u want to switch off the computer sir")

    # Input voice command
    take = self.takeCommand()
    choice = take
    if choice == 'yes':
        # Shutting down
        print("Shutting down the computer")
        self.Speak("Shutting the computer")
        os.system("shutdown /s /t 30")
    if choice == 'no':
        # Idle
        print("Thank u sir")
        self.Speak("Thank u sir")

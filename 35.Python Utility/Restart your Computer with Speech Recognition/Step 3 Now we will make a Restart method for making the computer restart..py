# Method to restart PC
def restart(self):
	self.Speak("do u want to restart the computer sir")
	take = self.takeCommand()
	choice = take
	if choice == 'yes':
		print("Restarting the computer")
		self.Speak("Restarting the computer")
		os.system("shutdown /r /t 30")
	if choice == 'no':
		print("Thank u sir")
		self.Speak("Thank u sir")

voice = speech.Recognizer()
with speech.Microphone() as source:
	print("Say something!")
	voice_command = voice.listen(source)

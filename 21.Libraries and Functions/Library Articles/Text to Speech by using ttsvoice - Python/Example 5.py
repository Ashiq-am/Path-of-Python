from ttsvoice import tts
file1 = open("temp.txt","r")
aa=file1.readlines()
for a in aa:
	tts(a,"male")

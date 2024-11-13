# import library
from pydub import AudioSegment

# Import audio file
wav_file = AudioSegment.from_file("Sample.wav")
''' 
	You can do anything like remixing and export 
	I'm increasing volume just for sake of my simplicity 
	Increase by 10 decibels 

'''
louder_wav_file = wav_file + 10

# Export louder audio file
louder_wav_file.export(out_f = "louder_wav_file.wav",
					format = "wav")

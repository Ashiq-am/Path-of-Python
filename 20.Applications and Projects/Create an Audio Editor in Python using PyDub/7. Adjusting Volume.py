from pydub import AudioSegment

# Load the audio file
audio = AudioSegment.from_file("input.wav", format="wav")

# Increase or decrease the volume of the audio
louder_audio = audio + 10

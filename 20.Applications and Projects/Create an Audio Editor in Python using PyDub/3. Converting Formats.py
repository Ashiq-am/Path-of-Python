from pydub import AudioSegment

# Load the audio file
audio = AudioSegment.from_file("input.wav", format="wav")

# Export the audio to a different format
audio.export("output.mp3", format="mp3")

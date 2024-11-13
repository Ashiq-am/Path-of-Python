from pydub import AudioSegment

# Load the audio file
audio = AudioSegment.from_file("input.wav", format="wav")

# Trim the audio to a specific duration
trimmed_audio = audio[1000:5000]

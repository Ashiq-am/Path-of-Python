from pydub import AudioSegment

# Load the audio file
audio = AudioSegment.from_file("input.wav", format="wav")

# Apply an effect to the audio
audio = audio.low_pass_filter(500)

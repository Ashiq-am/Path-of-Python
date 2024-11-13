from pydub import AudioSegment

# Load the audio files
audio1 = AudioSegment.from_file("input1.wav", format="wav")
audio2 = AudioSegment.from_file("input2.wav", format="wav")

# Concatenate the audio files
concatenated_audio = audio1 + audio2

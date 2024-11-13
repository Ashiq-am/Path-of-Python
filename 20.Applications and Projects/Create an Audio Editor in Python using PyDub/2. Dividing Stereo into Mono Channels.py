from pydub import AudioSegment

# Load the stereo audio file
audio = AudioSegment.from_file("input.wav", format="wav")

# Split the stereo audio into two mono channels
left_channel, right_channel = audio.split_to_mono()

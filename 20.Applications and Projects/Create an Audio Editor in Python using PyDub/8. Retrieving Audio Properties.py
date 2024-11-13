from pydub import AudioSegment

# Load the audio file
audio = AudioSegment.from_file("input.wav", format="wav")

# Get the duration, sample rate, and channels of the audio
duration = len(audio) # in milliseconds
sample_rate = audio.frame_rate # in Hz
channels = audio.channels # 1 for mono, 2 for stereo

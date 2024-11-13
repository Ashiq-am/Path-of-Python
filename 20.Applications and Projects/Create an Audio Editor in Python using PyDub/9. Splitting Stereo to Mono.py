from pydub import AudioSegment

# Load stereo audio file
stereo_audio = AudioSegment.from_file("stereo_audio.mp3", format="mp3")

# Split into mono channels
left_channel = stereo_audio.split_to_mono()[0]
right_channel = stereo_audio.split_to_mono()[1]

# Export mono channels
left_channel.export("left_channel.mp3", format="mp3")
right_channel.export("right_channel.mp3", format="mp3")

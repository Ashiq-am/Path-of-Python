from pydub import AudioSegment
from moviepy.editor import VideoFileClip

# Load the video file and extract its audio
video = VideoFileClip("input.mp4")
audio = video.audio

# Export the extracted audio
audio.write_audiofile("output.wav")

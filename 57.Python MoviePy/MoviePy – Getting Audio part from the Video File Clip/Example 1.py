# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")

# getting only first 3 seconds
clip = clip.subclip(0, 3)

# getting audio from the clip
audioclip = clip.audio

# printing audio clip
print(audioclip)

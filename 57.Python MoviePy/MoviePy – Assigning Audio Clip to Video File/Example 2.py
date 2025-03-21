# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")

# getting only first 5 seconds
clip = clip.subclip(0, 5)

# loading audio file
audioclip = AudioFileClip("allwell.mp3").subclip(0, 5)

# adding audio to the video clip
videoclip = clip.set_audio(audioclip)

# showing video clip
videoclip.ipython_display()

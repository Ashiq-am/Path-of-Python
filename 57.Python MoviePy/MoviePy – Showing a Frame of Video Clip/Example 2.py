# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")


# getting duration of the video
duration = clip.duration

# showing frame at 3 second
clip.show(3)

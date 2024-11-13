# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")


# getting duration of the video
duration = clip.duration

# printing duration
print("Duration : " + str(duration))

# showing final clip
clip.ipython_display()

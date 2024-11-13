# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")


# getting subclip from it
clip = clip.subclip(0, 5)


# altering time intervalr effect
final = clip.fl_time(lambda t: 2 * t)

# setting duration
final.duration = 10

# showing final clip
final.ipython_display()

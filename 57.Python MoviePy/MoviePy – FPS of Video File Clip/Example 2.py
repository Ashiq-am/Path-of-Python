# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")


# getting subclip from it
clip1 = clip.subclip(0, 7)

# getting frame rate of the clip
rate = clip1.fps

# printing the fps
print("FPS : " + str(rate))


print("---------------------------------------")


# showing final clip
clip1.ipython_display()

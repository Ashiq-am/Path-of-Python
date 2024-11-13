# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.webm").subclip(0, 10)


# getting frame rate of the clip
rate = clip.fps

# printing the fps
print("FPS : " + str(rate))


print("---------------------------------------")


# showing final clip
clip.ipython_display()

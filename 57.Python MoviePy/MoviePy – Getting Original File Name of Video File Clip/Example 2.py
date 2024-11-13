# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")


# getting subclip from it
clip1 = clip.subclip(0, 7)

# getting original file name of the clip
name = clip1.filename

# printing the name
print("File Name : " + name)


print("---------------------------------------")


# showing final clip
clip1.ipython_display()

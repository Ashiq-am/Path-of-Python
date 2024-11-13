# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.webm")

# getting subclip from it
clip1 = clip.subclip(0, 10)

# resizing the clip1
clip1 = clip1.resize(0.5)

# rotating the clip1
clip1 = clip1.rotate(180)

# getting original file name of the clip
name = clip1.filename

# printing the name
print("File Name : " + name)


print("---------------------------------------")


# showing final clip
clip1.ipython_display()

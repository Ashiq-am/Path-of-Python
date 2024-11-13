# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.mp4")

# getting only first 5 seconds
clip = clip.subclip(0, 5)

# getting end time of the clip
value = clip.end

# printing start time
print("End Time : ", end=" ")
print(value)

# showing clip
clip.ipython_display(width=360)

# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.webm")

# getting only first 5 seconds
clip1 = clip.subclip(0, 5)

# rotating clip by 180 degree to get the clip3
clip2 = clip1.rotate(180).set_start(4)

# adding cross fade of 2 seconds in the clip2
clip2 = clip2.crossfadein(2.0)

# creating a composite video
final = CompositeVideoClip([clip1, clip2])

# showing final clip
final.ipython_display(width = 480)

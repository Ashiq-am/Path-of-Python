# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.webm")

# getting only first 5 seconds
clip1 = clip.subclip(0, 5)

# rotating clip by 180 degree to get the clip3
clip2 = clip1.rotate(180)

# resizing the clip2 reducing it by 50 % clip2 = clip2.resize(0.5)

# setting start time to the clip2
clip2 = clip2.set_start(3)

# setting position of the clip2
clip2 = clip2.set_position((100, 100))

# creating a composite video
final = CompositeVideoClip([clip1, clip2])

# showing final clip
final.ipython_display(width = 480)

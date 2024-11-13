# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video and getting only first 5 seconds
clip1 = VideoFileClip("dsa_geek.webm").subclip(0, 5)

# rotating clip1 by 90 degree to get the clip2
clip2 = clip1.margin(40).set_start(3)

# rotating clip1 by 180 degree to get the clip3
clip3 = clip1.rotate(180).set_start(6)

# creating a composite video
final = CompositeVideoClip([clip2, clip1, clip3])

# showing final clip
final.ipython_display(width = 480)

# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")


# getting subclip from it
clip1 = clip.subclip(0, 5)

# mirroring image according to the y axis
clip2 = clip.fx(vfx.mirror_y).set_start(4)

# adding cross fade of 2 seconds in the clip2
clip2 = clip2.crossfadein(2.0)

# creating a composite video
final = CompositeVideoClip([clip1, clip2])

# showing final clip
final.ipython_display(width = 480)

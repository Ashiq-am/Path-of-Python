# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.webm")

# getting subclip as video is large
clip1 = clip.subclip(0, 5)

# getting subclip as video is large
clip2 = clip.subclip(60, 65)

# concatenating both the clips
final = concatenate_videoclips([clip1, clip2])

# showing final clip
final.ipython_display(width = 480)

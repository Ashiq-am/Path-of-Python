# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")

# getting only first 3 seconds
clip = clip.subclip(0, 3)

# saving video clip as gif
clip.write_gif("intro_gif.gif")

# loading gif
gif = VideoFileClip("intro_gif.gif")

# showing gif
gif.ipython_display()

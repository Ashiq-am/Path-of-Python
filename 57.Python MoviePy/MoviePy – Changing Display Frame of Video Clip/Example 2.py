# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")


# getting subclip from it
clip = clip.subclip(0, 5)

# method for inverting image
def invert_image(image):
	return image[:, :, [1, 2, 1]]

# inverting image
final = clip.fl_image(invert_image)

# showing final clip
final.ipython_display()

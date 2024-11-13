# Import everything needed to edit video clips
from moviepy.editor import *


# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.webm")

# getting only first 5 seconds
clip = clip.subclip(0, 5)

# method for inverting image
def invert_image(image):
	return image[:, :, [0, 2, 0]]

# inverting image
final = clip.fl_image(invert_image)

# showing final clip
final.ipython_display()

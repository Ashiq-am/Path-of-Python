# imporing the ImageSequence module:
from PIL import Image, ImageSequence

# Opening the input gif:
im = Image.open("animation.gif")

# create an index variable:
i = 1

# iterate over the frames of the gif:
for fr in ImageSequence.Iterator(im):
	fr.save("frame%d.png"%i)
	i = i + 1

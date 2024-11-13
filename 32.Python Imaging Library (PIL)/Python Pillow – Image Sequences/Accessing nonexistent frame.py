# imporing the ImageSequence module:
from PIL import Image, ImageSequence

# Opening the input gif:
im = Image.open("animation.gif")

# create an index variable:
i =1

# create an empty list to store the frames:
app = []

# iterate over the frames of the gif:
for fr in ImageSequence.Iterator(im):
	app.append(fr)
	fr.save("frame%d.png"%i)
	i = i + 1

# print the length of the list of frames.
print(len(app))

# nonexistent frame it will show
# IndexError
app[36].show()

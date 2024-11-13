# Import Image from wand.image module
from wand.image import Image

# Read first six frames of gif using Image() function
with Image(filename ='sample.gif[100x100 + 50 + 75]') as cropped_image:
	# convert gif file to png file
	cropped_image.convert("png")
	# save final image
	cropped_image.save(filename = 'final.png')

# Import Image from wand.image module
from wand.image import Image

# Read first six frames of gif using Image() function
with Image(filename ='initial.jpg[400x300]') as resized_image:
	# convert jpg image fie to png image file
	resized_image.convert("png")
	# save final image
	resized_image.save(filename = 'final.png')

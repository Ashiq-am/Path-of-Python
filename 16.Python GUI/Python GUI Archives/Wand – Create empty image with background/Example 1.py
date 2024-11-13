# import Image from wand.image module
from wand.image import Image

# create image using Image() function
with Image(width = 400, height = 300) as img:

	# Save image with a valid filename
	img.save(filename ='transparent.png')

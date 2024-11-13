# import Image from wand.image
from wand.image import Image

# read image using Image() function
with Image(filename = 'gog.png') as img:
	# resize image using resize() function
	img.resize(50, 50, filter = 'undefined, blur = 1')

	# save resized image
	img.save(filename = 'resized_gog.png')

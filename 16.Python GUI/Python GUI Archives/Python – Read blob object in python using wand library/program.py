# import required libraries
from __future__ import print_function

# import Image from wand.image module
from wand.image import Image

# open image using file handeling
with open('koala.jpeg') as f:

	# get blob from image file
	image_blob = f.read()

# read image using wand from blob file
with Image(blob = image_binary) as img:

	# get height of image
	print('height =', img.height)

	# get width of image
	print('width =', img.width)

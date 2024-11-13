# import Image from wand.image module
from wand.image import Image

# read image using Image function
with Image(filename ="frameman.jpeg") as img:

	# generate a grayscale image
	img.transform_colorspace('gray')

	# GENERATE EMBOSS IMAGE
	img.emboss(radius = 10, sigma = 3)

	# SAVE FINAL IMAGE
	img.save(filename ="manemboss.jpeg")

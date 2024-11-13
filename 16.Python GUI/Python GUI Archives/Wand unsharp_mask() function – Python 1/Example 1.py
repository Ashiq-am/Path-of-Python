# import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:

	# generating sharp image using unsharp_sharpen() function.
	img.unsharp_mask(radius = 10,
					sigma = 4,
					amount = 1,
					threshold = 0)
	img.save(filename ="unsharpmaskkoala.jpeg")

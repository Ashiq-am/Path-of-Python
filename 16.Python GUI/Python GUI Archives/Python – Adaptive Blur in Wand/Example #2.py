# import Image from wand.image module
from wand.image import Image

# read file using Image function
with Image(filename ="koala.jpeg") as img:

	# perform adaptive blur effect using adaptive_blur() function
	img.blur(radius = 8, sigma = 3)

	# save final image
	img.save(filename ="adblur_koala.jpeg")

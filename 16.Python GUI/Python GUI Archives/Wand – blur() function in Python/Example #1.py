# import Image from wand.image module
from wand.image import Image

# read file using Image function
with Image(filename ="koala.jpeg") as img:

	# perform blur effect using blur() function
	img.blur(radius = 0, sigma = 3)

	# save final image
	img.save(filename ="blur_koala.jpeg")

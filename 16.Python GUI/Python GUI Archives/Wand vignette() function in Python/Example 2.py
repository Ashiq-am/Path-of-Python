# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:

	# vignette image using vignette() function
	img.vignette(sigma = 10, x = 1, y = 1)
	img.save(filename ="vkoala2.jpeg")

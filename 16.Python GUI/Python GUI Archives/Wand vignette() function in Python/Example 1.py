# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:

	# vignette image using vignette() function
	img.vignette(sigma = 3, x = 10, y = 10)
	img.save(filename ="vkoala.jpeg")

# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="road.jpeg") as img:
	# vignette image using vignette() function
	img.enhance()
	img.save(filename ="vkoala2.jpeg")

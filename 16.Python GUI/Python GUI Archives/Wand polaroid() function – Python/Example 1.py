# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:
	# Polaroid image using polaroid() function
	img.polaroid()
	img.save(filename ="polkoala.jpeg")

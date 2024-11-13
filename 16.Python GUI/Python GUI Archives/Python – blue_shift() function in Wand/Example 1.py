# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:

	# Blueshift effect using blue_shift() function
	img.blue_shift(factor = 1.25)
	img.save(filename ="bs_koala.jpeg")

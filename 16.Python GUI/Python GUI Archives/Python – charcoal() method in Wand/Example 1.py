# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:

	# Charcoal fx using charcoal() function
	img.charcoal(radius = 1.5, sigma = 0.5)
	img.save(filename ="ch_koala.jpeg")

# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:

	# Charcoal fx using charcoal() function
	img.charcoal(radius = 4, sigma = 0.65)
	img.save(filename ="ch_koala_2.jpeg")

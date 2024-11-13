# Import Image from wand.image module
from wand.image import Image

# Read image using Image() function
with Image(filename ="koala.jpeg") as img:

	# Generate spread image using spread() function
	img.spread(radius = 16.0)
	img.save(filename ="spreadkoala2.jpg")

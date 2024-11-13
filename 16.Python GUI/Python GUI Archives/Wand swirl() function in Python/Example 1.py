# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:

	# swirl image using swirl() function
	img.swirl(degree =-90)
	img.save(filename ="wkoala.jpeg")

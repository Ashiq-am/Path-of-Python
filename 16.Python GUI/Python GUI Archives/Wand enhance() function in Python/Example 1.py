# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:
	# reduce noise image using enhance() function
	img.enhance()
	img.save(filename ="vkoala.jpeg")

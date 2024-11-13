# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:

	# imploded image using implode() function
	img.implode(amount = 0.35)
	img.save(filename ="impkoala.jpeg")

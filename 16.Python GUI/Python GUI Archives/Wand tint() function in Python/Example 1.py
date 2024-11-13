# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:

	# tinted image using tint() function
	img.tint(color ="yellow", alpha ="rgb(40 %, 60 %, 80 %)")
	img.save(filename ="tintkoala.jpeg")

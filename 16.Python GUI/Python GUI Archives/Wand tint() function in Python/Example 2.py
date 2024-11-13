# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:

	# implode imagefx using implode() function
	img.tint(color ="green", alpha ="rgb(10 %, 20 %, 40 %)")
	img.save(filename ="tint2.jpeg")

# import Image with wand.image module
from wand.image import Image

# read image using Image() function
with Image(filename ="koala.jpeg") as img:
	# generate colorized image
	img.colorize(color ="yellow", alpha ="rgb(10 %, 0 %, 20 %)")
	img.save(filename ="colorizedkoala.jpeg")

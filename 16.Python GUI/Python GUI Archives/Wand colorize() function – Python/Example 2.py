from wand.image import Image

# read image using Image() function
with Image(filename ="koala.jpeg") as img:
	# generate colorized image
	img.colorize(color ="yellow", alpha ="rgb(25 %, 0 %, 20 %)")
	img.save(filename ="colorizedkoala2.jpeg")

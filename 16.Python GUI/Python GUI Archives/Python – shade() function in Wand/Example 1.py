# import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:

	# generating shaded image using shade() function.
	img.shade(gray = True,
			azimuth = 286.0,
			elevation = 45.0)

	img.save(filename ="shadekoala.jpeg")

# import Image from wand.image module

from wand.image import Image

with Image(filename ="koala.jpeg") as img:
	# generating shaded image using shade() function.
	img.shade(gray = True,
			azimuth = 298.0,
			elevation = 70.0)

	img.save(filename ="shadekoala_2.jpeg")

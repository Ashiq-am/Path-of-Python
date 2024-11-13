# Import Image from wand.image module
from wand.image import Image

with Image(filename ="road.jpeg") as left:
	with left.clone() as right:
		with Image(width = 100, height = 1, pseudo ="plasma:") as affinity:

			# remap image using remap() function
			right.remap(affinity)
		left.extent(width = left.width * 2)

		# adding remaped image with original image
		left.composite(right, top = 0, left = right.width)
	left.save(filename ="roadr.jpeg")

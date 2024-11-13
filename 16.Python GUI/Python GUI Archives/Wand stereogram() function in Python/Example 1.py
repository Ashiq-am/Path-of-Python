# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as leftimg:

	with Image(filename ="koala.jpeg") as rightimg:
		# stereogram image using stereogram function
		with Image.stereogram(left = leftimg, right = rightimg) as img:
			img.save(filename ="fx-stereogram.jpg")

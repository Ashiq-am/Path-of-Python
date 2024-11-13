# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:
	with img.clone() as fimg:
		# flip image using flip() function
		fimg.flip()
		fimg.save(filename ='koalaflipped.jpeg')

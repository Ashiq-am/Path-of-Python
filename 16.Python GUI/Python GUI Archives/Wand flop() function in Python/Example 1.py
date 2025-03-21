# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:

	with img.clone() as fimg:
		# flopped image using flop() function
		fimg.flop()
		fimg.save(filename ='koalaflopped.jpeg')

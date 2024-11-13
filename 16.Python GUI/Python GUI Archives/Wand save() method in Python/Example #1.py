# import Image from wand.image module
from wand.image import Image

# read image using
with Image(filename ='koala.png') as img:
	# manipulate image
	img.rotate(90 * r)

	# save final image after
	img.save(filename ='final.png')

# import Image from wand.image module
from wand.image import Image

# read original file using Image() function
with Image(filename ='koala.jpg') as original:

	# creating clone image of original image
	with original.clone() as copy:

		# convert format of cloned image
		converted.format = 'png'

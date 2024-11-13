# Import Image from wand.image module
from wand.image import Image

# Create pseudo image using Image() function
with Image(width = 400, height = 300,
		pseudo ='gradient:# 32a852-# 09e846') as img:

	# Save image with a validfilename
	img.save(filename ='gradient.png')

# import Image from wand.image
from wand.image import Image
from wand.display import display

# read image using Image() function
with Image(filename = 'gog.png') as img:

	# crop image using crop() function
	img.crop(50, 50, 190, 170)

	# save resized image
	img.save(filename = 'croped_gog.png')
	display(img)

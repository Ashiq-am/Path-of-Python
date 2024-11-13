# import Image from wand.image
from wand.image import Image
from wand.display import display

# read image using Image() function
with Image(filename = 'koala.jpeg') as img:

	# cropping image using spliing operator
	with img[100:250, 120:250] as crpimg:
		crpimg.save(filename ='crpimg.jpg')

		# display image
		display(crpimg)

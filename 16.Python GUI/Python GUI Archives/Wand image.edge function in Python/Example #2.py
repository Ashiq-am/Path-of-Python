# import Image from wand.image module
from wand.image import Image

# read image using Image() function
with Image(filename ="koala.jpeg") as img:

	# transform image to grayscale image
	img.transform_colorspace('gray')

	# edge extraction using edge() function
	img.edge(3)
	img.save(filename ="edgekoala.jpeg")

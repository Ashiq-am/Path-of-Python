# import Image from wand.image module
from wand.image import Image

# read image using Image() function
with Image(filename ="koala.jpeg") as img:

	# apply kuwahara effect using kuwahara() function
	img.kuwahara(radius = 2, sigma = 1.5)
	img.save(filename ="koalakuwahara.jpg")

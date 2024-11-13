# import Image from wand.image module
from wand.image import Image

# read image using Image() function
with Image(filename ="koala.jpeg") as img:

	# apply kuwahara effect using kuwahara() function
	img.kuwahara(radius = 4, sigma = 3)
	img.save(filename ="koalakuwahara.jpg")

# import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:

	# generating sharp image using adaptive_sharpen() function.
	img.adaptive_sharpen(radius = 20, sigma = 10)
	img.save(filename ="askoala2.jpeg")

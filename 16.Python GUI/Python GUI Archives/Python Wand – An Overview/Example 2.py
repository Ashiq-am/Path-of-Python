# Import library from the wand
from wand.image import Image

# Import the image
with Image(filename ="geeksforgeeks.png") as pic:

	# Invoke blur function with radius 0 and sigma 3
	pic.blur(radius = 0, sigma = 3)

	# save the processed iamge
	pic.save(filename ="blur1.png")

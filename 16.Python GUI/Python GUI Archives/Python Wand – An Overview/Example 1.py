# Import library from the wand
from wand.image import Image

# Import the image
with Image(filename ='geeksforgeeks.png') as pic:

	# Read the image to fetch actual dimensions
	print('Width of the image:', pic.width)
	print('Height of the image:', pic.height)

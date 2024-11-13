# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as sharpen:
		# Invoke sharpen function with radius 50 and sigma 40
		sharpen.sharpen(50, 40)
		# Save the image
		sharpen.save(filename ='sharpen1.jpg')

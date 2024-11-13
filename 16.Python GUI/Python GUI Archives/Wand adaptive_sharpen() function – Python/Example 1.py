# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:

	# Clone the image in order to process
	with image.clone() as adaptive_sharpen:
		# Invoke adaptive_sharpen function with radius as 2, sigma as
		# 3 and channel as Green
		adaptive_sharpen.adaptive_sharpen(0, 3, 'Green')
		# Save the image
		adaptive_sharpen.save(filename ='adaptive_sharpen1.jpg')

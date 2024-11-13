# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:

	# Clone the image in order to process
	with image.clone() as adaptive_blur:
		# Invoke adaptive_blur function with radius as 2, sigma as
		# 3 and channel as Green
		adaptive_blur.adaptive_blur(int(0), int(3), 'Green')

		# Save the image
		adaptive_blur.save(filename ='adaptive_blur1.jpg')

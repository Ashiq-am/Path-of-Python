# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as blur:
		# Invoke blur function with radius as 10, sigma as 12
		# channel as 'Green'
		blur.blur(int(10), int(12), 'Green')
		# Save the image
		blur.save(filename ='blur1.jpg')

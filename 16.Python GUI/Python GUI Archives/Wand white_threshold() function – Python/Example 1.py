# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as white_threshold:
		# Invoke white_threshold function with "Green" color
		white_threshold.white_threshold("green")
		# Save the image
		white_threshold.save(filename ='white_threshold1.jpg')

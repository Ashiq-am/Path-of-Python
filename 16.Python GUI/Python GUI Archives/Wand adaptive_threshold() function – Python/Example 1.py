# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as adaptive_threshold:
		# Invoke adaptive_threshold function with width as 2, height as
		# 3 and offset as 2
		adaptive_threshold.adaptive_threshold(2, 3, 2)
		# Save the image
		adaptive_threshold.save(filename ='adaptive_threshold1.jpg')

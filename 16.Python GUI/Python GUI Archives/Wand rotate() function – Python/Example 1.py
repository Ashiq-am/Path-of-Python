# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as rotate:
		# Invoke rotate function
		rotate.rotate(45, 'red', True)
		# Save the image
		rotate.save(filename ='rotate1.jpg')

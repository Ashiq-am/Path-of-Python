# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as enhance:
		# Invoke enhance function
		enhance.enhance()
		# Save the image
		enhance.save(filename ='enhance1.jpg')

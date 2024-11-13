# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as transpose:
		# Invoke transpose function
		transpose.transpose()
		# Save the image
		transpose.save(filename ='transpose1.jpg')

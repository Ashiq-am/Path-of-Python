# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as posterize:
		# Invoke posterize function
		posterize.posterize(2, 'no')
		# Save the image
		posterize.save(filename ='posterize1.jpg')

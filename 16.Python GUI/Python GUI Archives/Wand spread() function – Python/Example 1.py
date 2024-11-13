# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as spread:
		# Invoke spread function with radius 15 and method as 'nearest'
		spread.spread(15, 'nearest')
		# Save the image
		spread.save(filename ='spread1.jpg')

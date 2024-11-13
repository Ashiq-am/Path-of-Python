# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as tint:
		# Invoke tint function with radius as 'green' and alpha as 'white'
		tint.tint('green', 'white')
		# Save the image
		tint.save(filename ='tint1.jpg')

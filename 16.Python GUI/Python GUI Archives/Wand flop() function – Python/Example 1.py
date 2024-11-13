# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as flop:
		# Invoke flop function
		flop.flop()
		# Save the image
		flop.save(filename ='flop1.jpg')

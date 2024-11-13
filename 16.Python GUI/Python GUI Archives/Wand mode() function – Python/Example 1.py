# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as mode:
		# Invoke mode function with width as 30 and height as 10
		mode.mode(30, 10)
		# Save the image
		mode.save(filename ='mode1.jpg')

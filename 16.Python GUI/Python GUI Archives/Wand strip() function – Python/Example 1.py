# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as strip:
		# Invoke strip function
		strip.strip()
		# Save the image
		strip.save(filename ='strip1.jpg')

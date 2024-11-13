# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as transverse:
		# Invoke transverse function
		transverse.transverse()
		# Save the image
		transverse.save(filename ='transverse1.jpg')

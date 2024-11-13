# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as deskew:
		# Invoke deskew function
		deskew.deskew(0.1)
		# Save the image
		deskew.save(filename ='deskew1.jpg')

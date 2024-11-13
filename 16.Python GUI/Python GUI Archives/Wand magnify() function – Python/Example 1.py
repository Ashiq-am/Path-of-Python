# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as magnify:
		# Invoke magnify function
		magnify.magnify()
		# Save the image
		magnify.save(filename ='magnify1.jpg')

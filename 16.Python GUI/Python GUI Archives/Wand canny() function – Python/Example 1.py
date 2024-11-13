# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as canny:
		# Invoke canny function
		canny.canny(3, 2, 0.2, 0.8)
		# Save the image
		canny.save(filename ='canny1.jpg')

# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as shade:
		# Invoke shade function
		shade.shade(True, 10, 15)
		# Save the image
		shade.save(filename ='shade1.jpg')

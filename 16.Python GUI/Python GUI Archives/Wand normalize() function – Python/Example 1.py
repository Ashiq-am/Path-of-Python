# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as normalize:

		# Invoke normalize function with Channel "green"
		normalize.normalize("green")

		# Save the image
		normalize.save(filename ='normalize1.jpg')

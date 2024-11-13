# Import library from the wand
from wand.image import Image

# Import the image
with Image(filename ='geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as flip:

		# Invoke flip function
		flip.flip()

		# Save the image
		flip.save(filename ='flip-geeksforgeeks.jpg')

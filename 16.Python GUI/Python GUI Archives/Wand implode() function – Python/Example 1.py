# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as implode:
		# Invoke implode function
		implode.implode(0.5, "blend")
		# Save the image
		implode.save(filename ='implode1.jpg')

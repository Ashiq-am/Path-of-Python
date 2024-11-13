# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as negate:
		# Invoke negate function with Channel "green"
		negate.negate(True, "green")
		# Save the image
		negate.save(filename ='negate1.jpg')

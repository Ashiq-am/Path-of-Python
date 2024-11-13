# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as clamp:
		# Invoke clamp function
		clamp.clamp("red")
		# Save the image
		clamp.save(filename ='clamp1.jpg')

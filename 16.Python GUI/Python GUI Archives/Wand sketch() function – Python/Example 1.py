# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as sketch:
		# Invoke sketch function
		sketch.sketch(15, 5, 10)
		# Save the image
		sketch.save(filename ='sketch1.jpg')

# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as scale:
		# Invoke scale function with threshold as 0.8
		scale.scale(200, 100)
		# Save the image
		scale.save(filename ='scale1.jpg')

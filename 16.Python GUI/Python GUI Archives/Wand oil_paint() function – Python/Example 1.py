# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as oil_paint:
		# Invoke oil_paint function with radius 6 and sigma 4
		oil_paint.oil_paint(6, 4)
		# Save the image
		oil_paint.save(filename ='oil_paint1.jpg')

# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as vignette:
		# Invoke vignette function with radius as 12, sigma as 10,
		# x as 20, y as 20
		vignette.vignette(12, 10, 20, 20)
		# Save the image
		vignette.save(filename ='vignette1.jpg')

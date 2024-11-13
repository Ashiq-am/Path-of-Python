# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as shear:
		# Invoke shear function
		shear.shear('Red', 20, 30)
		# Save the image
		shear.save(filename ='shear1.jpg')

# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as shave:
		# Invoke shave function
		shave.shave(50, 50)
		# Save the image
		shave.save(filename ='shave1.jpg')

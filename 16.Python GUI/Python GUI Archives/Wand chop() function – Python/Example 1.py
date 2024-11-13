# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as chop:
		# Invoke chop function
		chop.chop(300, 200, 15, 15)
		# Save the image
		chop.save(filename ='chop1.jpg')

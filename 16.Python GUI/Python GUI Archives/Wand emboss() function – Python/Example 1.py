# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as emboss:
		# Invoke emboss function
		emboss.emboss(0.1, 0.1)
		# Save the image
		emboss.save(filename ='emboss1.jpg')

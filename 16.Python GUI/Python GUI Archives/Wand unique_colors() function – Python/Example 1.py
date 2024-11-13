# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as unique_colors:
		# Invoke unique_colors function
		unique_colors.unique_colors()
		# Save the image
		unique_colors.save(filename ='unique_colors1.jpg')

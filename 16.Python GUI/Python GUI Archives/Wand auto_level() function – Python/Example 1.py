# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as auto_level:
		# Invoke auto_level function
		auto_level.auto_level()
		# Save the image
		auto_level.save(filename ='auto_level1.jpg')

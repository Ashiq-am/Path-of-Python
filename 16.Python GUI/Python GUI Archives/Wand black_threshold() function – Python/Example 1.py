# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as black_threshold:
		# Invoke black_threshold function with threshold parameter as 'Green'
		black_threshold.black_threshold('Green')
		# Save the image
		black_threshold.save(filename ='black_threshold1.jpg')

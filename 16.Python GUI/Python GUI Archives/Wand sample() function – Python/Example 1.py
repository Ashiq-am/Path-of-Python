# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as sample:
		# Invoke sample function with threshold as 0.8
		sample.sample(200, 100)
		# Save the image
		sample.save(filename ='sample1.jpg')

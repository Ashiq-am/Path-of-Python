# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as threshold:
		# Invoke threshold function with threshold as 0.3 and channel as 'green'
		threshold.threshold(0.3, 'green')
		# Save the image
		threshold.save(filename ='threshold1.jpg')

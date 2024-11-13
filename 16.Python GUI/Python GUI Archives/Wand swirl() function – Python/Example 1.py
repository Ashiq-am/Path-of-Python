# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as swirl:
		# Invoke swirl function with degree as 100 and method ss 'blend'
		swirl.swirl(100, 'blend')
		# Save the image
		swirl.save(filename ='swirl1.jpg')

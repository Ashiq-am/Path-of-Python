# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as blue_shift:
		# Invoke blue_shift function with radius as 10, sigma as 12
		# channel as 'Green'
		blue_shift.blue_shift(factor = 1.8)
		# Save the image
		blue_shift.save(filename ='blue_shift1.jpg')

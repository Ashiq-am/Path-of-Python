# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as mean_shift:
		# Invoke mean_shift function with width as 30 and height as 10
		# and color_distance as 0.2
		mean_shift.mean_shift(30, 10, 0.2)
		# Save the image
		mean_shift.save(filename ='mean_shift1.jpg')

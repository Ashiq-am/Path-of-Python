# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as solarize:
		# Invoke solarize function with threshold value 35
		solarize.solarize(35)
		# Save the image
		solarize.save(filename ='solarize1.jpg')

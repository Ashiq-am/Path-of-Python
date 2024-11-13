# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as shadow:
		# Invoke shadow function
		shadow.shadow(0.8, 0.2, 10, 40)
		# Save the image
		shadow.save(filename ='shadow1.jpg')

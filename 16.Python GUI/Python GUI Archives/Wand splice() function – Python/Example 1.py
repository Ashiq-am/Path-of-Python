# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as splice:
		# Invoke splice function with height as 20, width as 20, x as 10, y as 10
		splice.splice(20, 20, 10, 10)
		# Save the image
		splice.save(filename ='splice1.jpg')

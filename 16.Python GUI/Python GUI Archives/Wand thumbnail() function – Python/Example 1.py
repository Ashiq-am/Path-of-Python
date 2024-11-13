# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as thumbnail:
		# Invoke thumbnail function with x as 50 and y as 50
		thumbnail.thumbnail(50, 50)
		# Save the image
		thumbnail.save(filename ='thumbnail1.jpg')

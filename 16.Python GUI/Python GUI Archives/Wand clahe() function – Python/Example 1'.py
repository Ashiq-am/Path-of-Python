# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as clahe:
		# Invoke clahe function
		clahe.clahe(300, 200, 3.4, 2.7)
		# Save the image
		clahe.save(filename ='clahe1.jpg')

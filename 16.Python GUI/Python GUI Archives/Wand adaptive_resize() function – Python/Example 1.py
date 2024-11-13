# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as adaptive_resize:
		# Invoke adaptive_resize function with columns as 1024, rows as 768
		adaptive_resize.adaptive_resize(1024, 768)
		# Save the image
		adaptive_resize.save(filename ='adaptive_resize1.jpg')

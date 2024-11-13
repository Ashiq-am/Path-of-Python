# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as border:
		# Invoke border function border with color aas Green, Height as 12
		# Width as 18
		border.border('Green', int(12), int(18))
		# Save the image
		border.save(filename ='border1.jpg')

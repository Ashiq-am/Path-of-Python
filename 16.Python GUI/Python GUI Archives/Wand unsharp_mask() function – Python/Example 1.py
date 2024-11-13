# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as unsharp_mask:
		# Invoke unsharp_mask function with radius as 12, sigma as 10,
		# amount as 0.5, threshold as 0.8 and channel as 'Green'
		unsharp_mask.unsharp_mask(12, 10, 0.5, 0.8, 'Green')
		# Save the image
		unsharp_mask.save(filename ='unsharp_mask1.jpg')

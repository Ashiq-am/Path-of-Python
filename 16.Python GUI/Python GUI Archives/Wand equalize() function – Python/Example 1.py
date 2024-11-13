# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as equalize:
		# Invoke equalize function with channel as "green"
		equalize.equalize("green")
		# Save the image
		equalize.save(filename ='equalize1.jpg')

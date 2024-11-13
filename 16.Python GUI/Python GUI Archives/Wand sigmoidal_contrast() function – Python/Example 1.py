# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as sigmoidal_contrast:
		# Invoke sigmoidal_contrast function
		sigmoidal_contrast.sigmoidal_contrast(True, 10, 10)
		# Save the image
		sigmoidal_contrast.save(filename ='sigmoidal_contrast1.jpg')

# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as wave:
		# Invoke wave function with amplitude as 12, wavelength as 15
		# method as 'bilinear'
		wave.wave(12, 15, 'bilinear')
		# Save the image
		wave.save(filename ='wave1.jpg')

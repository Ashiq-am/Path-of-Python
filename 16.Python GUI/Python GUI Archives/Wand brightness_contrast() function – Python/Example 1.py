# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as brightness_contrast:
		# Invoke brightness_contrast function with brightness as 50, Contrast as 17
		# channel as Red
		brightness_contrast.brightness_contrast(int(50), int(17), 'Red')
		# Save the image
		brightness_contrast.save(filename ='brightness_contrast1.jpg')

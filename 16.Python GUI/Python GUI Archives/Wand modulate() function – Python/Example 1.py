# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as modulate:
		# Invoke modulate function with brightness 30 %, saturation 45 %, hue 25 % modulate.modulate(30, 45, 25)
		# Save the image
		modulate.save(filename ='modulate1.jpg')

# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as sepia_tone:
		# Invoke sepia_tone function with threshold as 0.8
		sepia_tone.sepia_tone(0.8)
		# Save the image
		sepia_tone.save(filename ='sepia_tone1.jpg')

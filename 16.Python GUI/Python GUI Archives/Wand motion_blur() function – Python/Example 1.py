# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as motion_blur:
		# Invoke motion_blur function with radius 25, sigma 3 and angle 45
		motion_blur.motion_blur(25, 3, 45)
		# Save the image
		motion_blur.save(filename ='motion_blur1.jpg')

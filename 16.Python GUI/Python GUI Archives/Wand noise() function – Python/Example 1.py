# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as noise:
		# Invoke noise function with Channel "green" and noise poisson
		noise.noise("poisson", 2, "green")
		# Save the image
		noise.save(filename ='noise1.jpg')

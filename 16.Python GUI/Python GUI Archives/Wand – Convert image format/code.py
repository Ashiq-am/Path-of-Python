# import Image from wand.image module
from wand.image import Image

# Read .png image using Image() function
with Image(filename ='koala.png') as img:

	# Change format in python using format property
	img.format = 'jpeg'

	# Save final image
	img.save(filename ='koala.jpg')

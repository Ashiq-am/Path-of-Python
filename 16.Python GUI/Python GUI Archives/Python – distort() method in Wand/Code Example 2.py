# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="gog.png") as img:
	arguments = (0, 0, 20, 60,
				90, 0, 70, 63,
				0, 90, 5, 83,
				90, 90, 85, 88)
	img.distort('perspective', arguments)
	img.save(filename ='gogdistort.png')

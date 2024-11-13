# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="gog.png") as img:
	img.distort('arc', (45, ))
	img.save(filename ='gogdistort1.png')

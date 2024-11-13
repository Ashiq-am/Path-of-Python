# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="rd.jpg") as img:
	img.virtual_pixel = 'tile'
	img.distort('arc', (60, ))
	img.save(filename ='rdsv2.jpg')

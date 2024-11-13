from wand.color import Color
# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="gog.png", background = Color("green")) as img:

	img.virtual_pixel = 'checker_tile'
	img.distort('arc', (60, ))
	img.save(filename ='rdsv.jpg')

from wand.color import Color
# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="gog.png") as img:
	img.matte_color = Color('BLUE')
	img.virtual_pixel = 'tile'
	args = (0, 0, 30, 60, 140, 0, 110, 60,
			0, 92, 2, 90, 140, 92, 138, 90)
	img.distort('perspective', args)
	img.save(filename ="rdmc.jpg")

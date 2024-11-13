# Import Color from wand.color module
from wand.color import Color
# Import Image from wand.image module
from wand.image import Image

with Image(filename ='gog.png') as img:
	img.resize(140, 92)
	img.background_color = Color('skyblue')
	img.virtual_pixel = 'background'
	args = (
		20, 21, 12, 11, # Point 1: (10, 10) => (15, 15)
		38, 1, 17, 0, # Point 2: (139, 0) => (100, 20)
		7, 92, 50, 80 # Point 3: (0, 92) => (50, 80)
	)
	# affline distortion using distort function
	img.distort('affine', args)
	img.save(filename ="afflinegfg2.png")

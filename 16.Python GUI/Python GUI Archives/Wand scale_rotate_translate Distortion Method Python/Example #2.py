# Import Color from wand.color module
from wand.color import Color
# Import Image from wand.image module
from wand.image import Image

with Image(filename ='gog.png') as img:
	img.resize(140, 92)
	img.background_color = Color('skyblue')
	img.virtual_pixel = 'background'
	angle = 90.0
	scale = 0.5

	# scale_rotate_translate method using distort function
	img.distort('scale_rotate_translate', (scale, angle, ))
	img.save(filename ="srtgfg2.png")

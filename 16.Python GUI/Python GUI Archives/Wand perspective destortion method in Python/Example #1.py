# Import Color from wand.color module
from wand.color import Color
# Import Image from wand.image module
from wand.image import Image

with Image(filename ='gog.png') as img:
	img.virtual_pixel = 'background'
	img.background_color = Color('green')
	img.matte_color = Color('skyblue')
	arguments = (0, 0, 20, 60,
				90, 0, 70, 63,
				0, 90, 5, 83,
				90, 90, 85, 88)
	# perspective distortion using distort function
	img.distort('perspective', arguments)
	img.save(filename ='gfg_p.png')

# import Color from wand.color module
from wand.color import Color
# import Image from wand.image module
from wand.image import Image

clr = Color('green')
with Image(width = 400, height = 300, background = clr) as img:
	img.save(filename ='green.png')

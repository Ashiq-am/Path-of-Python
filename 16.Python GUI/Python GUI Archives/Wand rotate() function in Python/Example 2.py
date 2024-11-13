# Import Image from wand.image module
from wand.image import Image
from wand.color import Color

with Image(filename ="koala.jpeg") as img:
	with img.clone() as rotated:
		# rotate image using rotate() function
		rotated.rotate(135, background = Color('rgb(229, 221, 112)'))
		rotated.save(filename ='transform-rotated-135.jpg')

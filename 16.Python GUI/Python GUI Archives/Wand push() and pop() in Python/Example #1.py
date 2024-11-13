from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

with Drawing() as ctx:
	ctx.fill_color = Color('RED')
	ctx.stroke_color = Color('BLACK')
	ctx.push()

	ctx.circle((50, 50), (25, 25))
	ctx.pop()

	ctx.fill_color = Color('YELLOW')
	ctx.stroke_color = Color('GREEN')
	ctx.push()

	ctx.circle((150, 150), (125, 125))
	ctx.pop()

	with Image(width = 200, height = 200, background = Color('lightgreen')) as image:
		ctx(image)
		image.save(filename = "push.png")

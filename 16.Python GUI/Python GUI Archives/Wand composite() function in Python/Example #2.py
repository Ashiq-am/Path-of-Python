from wand.image import Image, COMPOSITE_OPERATORS
from wand.drawing import Drawing
from wand.display import display

gog = Image(filename ='gog.png')
road = Image(filename ='rd.jpg')

g = gog.clone()
r = road.clone()
with Drawing() as draw:
	# composite image with dissolve operator
	draw.composite(operator = 'luminize', left = 20, top = 30,width = g.width, height = g.height, image = g)
	draw(r)
	r.save(filename ="dissolve.png")
	display(r)

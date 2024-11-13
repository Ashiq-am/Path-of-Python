from wand.image import Image, COMPOSITE_OPERATORS
from wand.drawing import Drawing
from wand.display import display

gog = Image(filename ='gog.png')
road = Image(filename ='rd.jpg')

g = gog.clone()
r = road.clone()
with Drawing() as draw:
	# composite image with color_burn operator
	draw.composite(operator ='color_burn', left = 20, top = 30,width = r.width, height = r.height, image = r)
	draw(g)
	g.save(filename ="colorburn.png")
	display(g)

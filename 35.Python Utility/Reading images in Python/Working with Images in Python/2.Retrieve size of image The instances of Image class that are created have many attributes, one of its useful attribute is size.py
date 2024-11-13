from PIL import Image

filename = "image.png"
with Image.open(filename) as image:
	width, height = image.size
#Image.size gives a 2-tuple and the width, height can be obtained

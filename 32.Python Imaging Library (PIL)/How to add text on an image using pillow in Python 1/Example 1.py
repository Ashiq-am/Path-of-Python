from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# importing the image
img = Image.open("gfg.png")
draw = ImageDraw.Draw(img)

# specifying coordinates and colour of text
draw.text((50, 90), "Sample Text", (255, 255, 255))

# saving the image
img.save('sample.jpg')

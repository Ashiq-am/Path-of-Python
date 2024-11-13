from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# importing the image
img = Image.open("gfg.png")
draw = ImageDraw.Draw(img)

# loading the font and providing the size
font = ImageFont.truetype("ComicSansMS3.ttf", 30)

# specifying coordinates and colour of text
draw.text((50, 90), "Hello World!", (255, 255, 255), font=font)

# saving the image
img.save('sample.jpg')

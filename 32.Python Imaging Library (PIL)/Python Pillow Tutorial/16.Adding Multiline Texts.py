# Importing Image and ImageFont, ImageDraw
# module from PIL package
from PIL import Image, ImageFont, ImageDraw

# creating a image object
image = Image.open(r'geek.jpg')

draw = ImageDraw.Draw(image)

# specified font size
font = ImageFont.truetype(r'DroidSans.ttf', 15)

text = u"""\
Geeks
FOR \n Geeks"""

# drawing text size
draw.text((6, 8), text, fill ="red", font = font, align ="right")

image.show()

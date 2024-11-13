
# Importing Image and ImageFont, ImageDraw module from PIL package
from PIL import Image, ImageFont, ImageDraw

# creating a image object
image = Image.open(r'C:\Users\System-Pc\Desktop\flower.jpg')

draw = ImageDraw.Draw(image)

# specified font size
font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 15)
spacing = 50
text = u"""\
ALWAYS BE HAPPY
(LAUGHING IS THE \n BEST MEDICINE)"""

# drawing text size
draw.text((6, 8), text, fill ="black",
          font = font, spacing = spacing, align ="right")

image.show()

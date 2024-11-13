
# Importing Image and ImageFont, ImageDraw module from PIL package
from PIL import Image, ImageFont, ImageDraw

# creating a image object
image = Image.open(r'C:\Users\System-Pc\Desktop\rose.jpg')

draw = ImageDraw.Draw(image)

# specified font size
font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 20)

text = 'LAUGHING IS THE \n BEST MEDICINE'

# drawing text size
draw.text((5, 5), text, font = font, align ="left")

image.show()

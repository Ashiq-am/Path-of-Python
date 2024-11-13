# Importing Image and ImageFont, ImageDraw module from PIL package
from PIL import Image, ImageFont, ImageDraw

# creating a image object
image = Image.open(r'C:\Users\System-Pc\Desktop\rose.jpeg')

draw = ImageDraw.Draw(image)

font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 70)

text = 'DO NOT DRINK AND \nDRIVE'

draw.text((10, 20), text, font=font)

image.show()

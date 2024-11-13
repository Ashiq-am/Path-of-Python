# Import required Image library
from PIL import Image, ImageDraw, ImageFont

# Create an Image Object from an Image
im = Image.open('nature.jpg')
width, height = im.size

draw = ImageDraw.Draw(im)
text = "lovely nature"

font = ImageFont.truetype('arial.ttf', 36)
textwidth, textheight = draw.textsize(text, font)

# calculate the x,y coordinates of
# the text
x = 100
y = 50

# draw watermark in the bottom right
# corner
draw.text((x, y), text, font=font)
im.show()

# Save watermarked image
im.save('watermark.jpg')

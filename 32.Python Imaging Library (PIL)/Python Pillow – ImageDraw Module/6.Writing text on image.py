# Importing Image, ImageDraw and ImageFont
# from PIL
from PIL import Image, ImageDraw, ImageFont

# Opening the image to be used
img = Image.open('img_path.png')

# Creating an instance for
# the font to be used using ImageFont
# Here we pass the font name and
# the font size as arguments
fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 20)

# Creating a Draw object
draw = ImageDraw.Draw(img)

# Drawing the text on the image
draw.text(xy=(25, 160),
		text="Hello, Geeks!",
		font=fnt,
		fill=(0, 127, 0))

img.show()

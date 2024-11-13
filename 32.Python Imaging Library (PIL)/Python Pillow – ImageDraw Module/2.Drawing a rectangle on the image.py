# Importing Image and ImageDraw from PIL
from PIL import Image, ImageDraw

# Opening the image to be used
img = Image.open('img_path.png')

# Creating a Draw object
draw = ImageDraw.Draw(img)

# Drawing a green rectangle
# in the middle of the image
draw.rectangle(xy = (50, 50, 150, 150),
			fill = (0, 127, 0),
			outline = (255, 255, 255),
			width = 5)

# Method to display the modified image
img.show()

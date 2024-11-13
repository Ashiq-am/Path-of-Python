# Importing Image and ImageDraw from PIL
from PIL import Image, ImageDraw

# Opening the image to be used
img = Image.open('img_path.png')

# Creating a Draw object
draw = ImageDraw.Draw(img)

# Drawing a green vertical
# line in the middle image
draw.line(xy=(50, 150, 150, 50),
		fill=(0, 128, 0), width = 5)

# Method to display the modified image
img.show()

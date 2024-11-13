# Importing Image and ImageDraw from PIL
from PIL import Image, ImageDraw

# Opening the image to be used
img = Image.open('img_path.png')

# Creating a Draw object
draw = ImageDraw.Draw(img)

# Drawing a green diamond-shaped
# polygon in the middle of the image
draw.polygon(xy=(50, 150, 150, 50),
			fill=(0, 128, 0),
			outline=(255, 255, 255))

# Method to display the modified image
img.show()

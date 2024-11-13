from PIL import Image

# Open image
im = Image.open("nature.jpg")

# Show actual Image
im.show()

# Show cropped Image
im = im.crop((0,0,50,50))
im.show()

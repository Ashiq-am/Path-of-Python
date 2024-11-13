from PIL import Image

# Open image
im = Image.open("nature.jpg")

# Show actual Image
im.show()

# Show rotated Image
im = im.rotate(45)
im.show()

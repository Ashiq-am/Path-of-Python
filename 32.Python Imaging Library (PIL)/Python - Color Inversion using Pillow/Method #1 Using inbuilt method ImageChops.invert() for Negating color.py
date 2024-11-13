# Importing imagechops for using the invert() method
from PIL import Image, ImageChops

# Opening the test image, and saving it's object
img = Image.open('test.jpg')

# Passing the image object to invert()
inv_img = ImageChops.invert(img)

# Displaying the output image
inv_img.show()

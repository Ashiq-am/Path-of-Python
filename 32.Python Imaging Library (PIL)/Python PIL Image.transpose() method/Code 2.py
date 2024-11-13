# Improting Image class from PIL module
from PIL import Image

# Opens a image in RGB mode
im = Image.open(r"C:\Users\System-Pc\Desktop\flower1.jpg")

# Size of the image in pixels (size of orginal image)
# (This is not mandatory)
width, height = im.size

# Setting the points for cropped image
left = 3
top = height / 2
right = 164
bottom = 3 * height / 2

# Cropped image of above dimension
# (It will not change orginal image)
im1 = im.crop((left, top, right, bottom))
newsize = (1800, 1800)
im1 = im1.transpose(Image.FLIP_TOP_BOTTOM)
# Shows the image in image viewer
im1.show()

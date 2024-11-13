# Importing Image and ImageGrab module from PIL package
from PIL import Image, ImageGrab

# using the grabclipboard method
im = ImageGrab.grabclipboard()

im.show()

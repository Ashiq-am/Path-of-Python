# We import necessary libraries.
# The PIL Library is used to read the images
from PIL import Image
import pytesseract

# Read the image
image = Image.open(r'pic.png')

# Perform the information extraction from images
# Note below, put the address where tesseract.exe
# file is located in your system
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print(pytesseract.image_to_string(image))

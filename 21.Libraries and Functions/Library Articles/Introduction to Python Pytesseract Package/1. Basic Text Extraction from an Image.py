from PIL import Image
import pytesseract

# Load an image
img = Image.open('image.png')

# Extract text from image
text = pytesseract.image_to_string(img)

print(text)

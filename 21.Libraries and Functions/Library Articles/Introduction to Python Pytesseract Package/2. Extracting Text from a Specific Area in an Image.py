from PIL import Image
import pytesseract

# Load an image
img = Image.open('image.png')

# Define the region of interest (left, upper, right, lower)
roi = img.crop((50, 50, 300, 300))

# Extract text from the cropped region
text = pytesseract.image_to_string(roi)

print(text)

from PIL import Image, ImageFilter, ImageEnhance
import pytesseract

# Load an image with noise or low contrast
img = Image.open('noisy_image.jpg')

# Convert the image to grayscale
img = img.convert('L')

# Apply a median filter to reduce noise
img = img.filter(ImageFilter.MedianFilter())

# Enhance the image contrast
enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(2)

# Extract text from the pre-processed image
text = pytesseract.image_to_string(img)

print(text)

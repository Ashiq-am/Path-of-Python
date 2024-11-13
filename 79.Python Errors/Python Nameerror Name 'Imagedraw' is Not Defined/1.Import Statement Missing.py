# Incorrect
from PIL import Image

img = Image.new('RGB', (100, 100))
draw = ImageDraw.Draw(img) # Raises NameError

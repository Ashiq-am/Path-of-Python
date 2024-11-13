from PIL import Image, ImageDraw

img = Image.new('RGB', (100, 100))
draw = ImageDraw.Draw(img) # No NameError

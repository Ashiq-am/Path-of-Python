from PIL import Image, ImageDraw as Drawing

img = Image.new('RGB', (100, 100))
draw = Drawing.Draw(img) # No NameError

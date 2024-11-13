from PIL import Image

with Image.open("gfg.png") as image:
    width, height = image.size

print((width, height))

from PIL import Image

img = Image.open("gfg.png")
width, height = img.size

# resizing the image
img = img.resize((width // 2, height // 2))

img.save("resized_picture.png")

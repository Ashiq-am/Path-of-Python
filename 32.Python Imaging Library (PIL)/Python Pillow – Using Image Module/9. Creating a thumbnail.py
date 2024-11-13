from PIL import Image

img = Image.open("gfg.png")

img.thumbnail((200, 200))

img.save("thumb.png")

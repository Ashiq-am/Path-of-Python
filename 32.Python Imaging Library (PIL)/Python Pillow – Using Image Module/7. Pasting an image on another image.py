from PIL import Image

img1 = Image.open("gfg.jpg")

#pasting img2 on img1
img2 = Image.open("gfg.png")
img1.paste(img2, (50, 50))

img1.save("pasted_picture.jpg")

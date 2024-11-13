from PIL import Image

img = Image.open("gfg.png")

# flipping the image by 180 degree horizontally
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

transposed_img.save("transposed.png")

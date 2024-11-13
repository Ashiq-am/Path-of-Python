from PIL import Image


angle = 40
img = Image.open(r"test.png")
r_img = img.rotate(angle)

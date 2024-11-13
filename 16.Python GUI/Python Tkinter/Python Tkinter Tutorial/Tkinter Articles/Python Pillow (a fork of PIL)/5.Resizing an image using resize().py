from PIL import Image


size = (40, 40)
img = Image.open(r"test.png")
r_img = img.resize(size)

r_img.show()

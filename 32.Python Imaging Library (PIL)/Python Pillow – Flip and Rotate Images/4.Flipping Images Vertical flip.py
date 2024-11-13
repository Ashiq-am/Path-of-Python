from PIL import Image


img = Image.open('geek.jpg')

# flip vertical
flip_img = img.transpose(Image.FLIP_TOP_BOTTOM)

flip_img.show()

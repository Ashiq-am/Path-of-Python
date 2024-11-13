from PIL import Image


img = Image.open('geek.jpg')

# flip horizontal
flip_img = img.transpose(Image.FLIP_LEFT_RIGHT)

flip_img.show()

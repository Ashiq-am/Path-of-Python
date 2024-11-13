from PIL import Image


img = Image.open('geek.jpg')

# flip anti-clockwise
flip_img = img.transpose(Image.TRANSPOSE)

flip_img.show()

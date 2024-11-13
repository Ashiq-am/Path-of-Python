from PIL import Image


img = Image.open('geek.jpg')

# flip clockwise
flip_img= img.transpose(Image.TRANSVERSE)

flip_img.show()

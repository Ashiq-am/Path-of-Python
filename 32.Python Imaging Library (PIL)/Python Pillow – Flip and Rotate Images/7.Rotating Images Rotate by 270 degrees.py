from PIL import Image


img = Image.open('geek.jpg')

# rotate by 270 degrees
rot_img = img.transpose(Image.ROTATE_270)

rot_img.show()

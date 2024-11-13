from PIL import Image


img = Image.open('geek.jpg')

# rotate by 180 degrees
rot_img = img.transpose(Image.ROTATE_180)

rot_img.show()

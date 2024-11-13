from PIL import Image


img = Image.open('geek.jpg')

# rotate by 90 degrees
rot_img = img.transpose(Image.ROTATE_90)

rot_img.show()

from PIL import Image
image = Image.open('nature.jpg')
image.show()

image.save('nature1.bmp')
image1 = Image.open('nature1.bmp')
image1.show()

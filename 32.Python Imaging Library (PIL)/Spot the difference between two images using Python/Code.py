# import module
from PIL import Image, ImageChops

# assign images
img1 = Image.open("1img.jpg")
img2 = Image.open("2img.jpg")

# finding difference
diff = ImageChops.difference(img1, img2)

# showing the difference
diff.show()

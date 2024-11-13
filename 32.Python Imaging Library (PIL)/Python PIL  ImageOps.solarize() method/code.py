# Importing Image and ImageOps module from PIL package
from PIL import Image, ImageOps

# creating a image1 object
im1 = Image.open(r"C:\Users\System-Pc\Desktop\a.JPG")

# image segmentation
# using threshold value = 130
# applying solarize method
im2 = ImageOps.solarize(im1, threshold=130)

im2.show()

# Importing Image and ImageOps module from PIL package
from PIL import Image, ImageOps

# creating a image1 object
im1 = Image.open(r"C:\Users\System-Pc\Desktop\circleimage.PNG")

# applying fit method
# Setting width = 100 and height = 100
im2 = ImageOps.fit(im1, (100, 100), method = 0,
				bleed = 0.0, centering =(0.5, 0.5))

im2.show()

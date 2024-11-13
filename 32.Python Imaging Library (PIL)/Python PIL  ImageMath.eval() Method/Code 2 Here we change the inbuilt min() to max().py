# Importing Image module from PIL package
from PIL import Image, ImageMath

# creating a image object
im1 = Image.open(r"C:\Users\System-Pc\Desktop\ybear.jpg").convert('L')
im2 = Image.open(r"C:\Users\System-Pc\Desktop\leave.jpg").convert('L')

# applying the eval method

out = ImageMath.eval("convert(max(a, b), 'L')", a = im1, b = im2)
out.save("result.jpg")
out.show()

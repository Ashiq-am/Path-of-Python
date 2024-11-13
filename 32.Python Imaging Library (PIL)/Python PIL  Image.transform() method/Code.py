
# importing Image module from PIL package
from PIL import Image

# creating image object
img = Image.open(r"C:\Users\System-Pc\Desktop\tree.jpg")

# using image transform method
img1 = img.transform((300, 300), Image.EXTENT,
	data =[10, 0, 10 + img.width // 4, img.height // 3 ])

img1.show()

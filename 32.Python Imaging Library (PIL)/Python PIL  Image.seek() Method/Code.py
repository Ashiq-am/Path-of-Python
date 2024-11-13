

# importing image class from PIL package
from PIL import Image

# creating gif image object
img = Image.open(r"C:\Users\System-Pc\Desktop\time.gif")
img1 = img.tell()
print(img1)

# using seek() method
img2 = img.seek(img.tell() + 1)
img3 = img.tell()
print(img3)
img.show()

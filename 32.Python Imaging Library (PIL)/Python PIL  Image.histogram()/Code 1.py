

from PIL import Image

img = Image.open(r"C:\Users\System-Pc\Desktop\tree.jpg")
r, g, b = img.split()
len(r.histogram())
### 256 ###

r.histogram()

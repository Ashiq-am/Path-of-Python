

# importing image object from PIL
from PIL import Image

# using tobytes data as raw for frombyte function
tobytes = b'\xbf\x8cd\xba\x7f\xe0\xf0\xb8t\xfe'
img = Image.frombytes("L", (3, 2), tobytes)

# creating list
img1 = list(img.getdata())
print(img1)

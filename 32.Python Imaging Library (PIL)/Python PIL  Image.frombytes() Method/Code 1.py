

# importing image object from PIL
from PIL import Image

# using tobytes data as raw for frombyte function
tobytes = b'xd8\xe1\xb7\xeb\xa8\xe5 \xd2\xb7\xe1'
img = Image.frombytes("L", (3, 2), tobytes)

# creating list
img1 = list(img.getdata())
print(img1)

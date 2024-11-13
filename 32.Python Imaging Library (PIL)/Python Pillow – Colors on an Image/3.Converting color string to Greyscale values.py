# importing module
from PIL import ImageColor

# using getrgb for yellow
img1 = ImageColor.getcolor("yellow",'L')
print(img1)

# using getrgb for red
img2 = ImageColor.getcolor("red",'L')
print(img2)

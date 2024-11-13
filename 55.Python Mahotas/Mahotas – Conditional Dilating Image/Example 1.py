# importing required libraries
# importing required libraries
import mahotas
import mahotas.demos
from pylab import gray, imshow, show
import numpy as np

# loading image
img = mahotas.demos.load('lena')

# grey image
g = img[:, :, 1]

# multiplying grey image values
g = g * 100

# filtering image
img = img.max(2)

# otsu method
T_otsu = mahotas.otsu(img)


# image values should be greater than otsu value
img = img > T_otsu

print("Image threshold using Otsu Mehtod")

# showing image
imshow(img)
show()

# dilating image using conditional grey image
dilate_img = mahotas.cdilate(img, g)

# showing dilated image
print("Dilated Image")
imshow(dilate_img)
show()

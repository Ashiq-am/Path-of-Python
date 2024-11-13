# importing required libraries
# importing required libraries
import mahotas
import mahotas.demos
from pylab import gray, imshow, show
import numpy as np

# loading iamge
img = mahotas.demos.load('lena')

# grey image
g = img[:, :, 1]

# multiplying grey image values
g = g * 3

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

# eroding image using conditional grey image
new_img = mahotas.cerode(img, g)

# showing eroded image
print("Eroded Image")
imshow(new_img)
show()

# importing required libraries
import mahotas
import mahotas.demos
from pylab import gray, imshow, show
import numpy as np

# loading image
luispedro = mahotas.demos.load('luispedro')

# filtering image
luispedro = luispedro.max(2)

# otsu method
T_otsu = mahotas.otsu(luispedro)

# image values should be greater than otsu value
img = luispedro > T_otsu

print("Image threshold using Otsu Mehtod")

# showing image
imshow(img)
show()

# closing image
new_img = mahotas.morph.close(img)

# showing new image
print("Closed Image")
imshow(new_img)
show()

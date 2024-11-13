# importing required libraries
import mahotas
import mahotas.demos
from pylab import gray, imshow, show
import numpy as np
import matplotlib.pyplot as plt

# loading image
img = mahotas.demos.load('lena')



# filtering image
img = img.max(2)

print("Image")

# showing image
imshow(img)
show()

# resizing image
new_img = mahotas.imresize(img, [200, 250])


# showing image
print("Resized Image")
imshow(new_img)
show()

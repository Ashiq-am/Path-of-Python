# importing required libraries
import mahotas
import numpy as np
from pylab import gray, imshow, show
import os
import matplotlib.pyplot as plt

# loading image
img = mahotas.imread('dog_image.png')


# filtering image
img = img[:, :, 0]

print("Image")

# showing image
imshow(img)
show()
# template
template = np.array([
			[1, 1, 1],
			[1, 1, 1],
			[1, 1, 1]], bool)

# matching template
new_img = mahotas.template_match(img, template)


# showing image
print("Matched Image")
imshow(new_img)
show()

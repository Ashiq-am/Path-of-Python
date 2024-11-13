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

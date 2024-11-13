# importing required libraries
import mahotas
import mahotas.demos
from pylab import gray, imshow, show
import numpy as np

# loading image
img = mahotas.demos.load('lena')



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

# template
template = np.array([
		[0, 1, 1],
		[0, 1, 1],
		[0, 1, 1]], bool)


# finding template in the image
new_img = mahotas.find(img, template)

print("Image with only templates")
# showing new image
imshow(new_img)
show()

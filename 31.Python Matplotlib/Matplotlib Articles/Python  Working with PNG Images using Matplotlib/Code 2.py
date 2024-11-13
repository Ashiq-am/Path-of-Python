# importing pyplot and image from matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as img

# reading png image
im = img.imread('imR.png')

# applying pseudocolor
# default value of colormap is used.
lum = im[:, :, 0]

# show image
plt.imshow(lum)

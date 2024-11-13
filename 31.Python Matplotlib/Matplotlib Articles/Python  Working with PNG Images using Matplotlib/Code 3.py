# importing pyplot and image from matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as img

# reading png image
im = img.imread('imR.png')
lum = im[:, :, 0]

# setting colormap as hot
plt.imshow(lum, cmap ='hot')
plt.colorbar()

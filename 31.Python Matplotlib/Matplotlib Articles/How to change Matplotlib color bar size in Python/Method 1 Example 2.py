import matplotlib.pyplot as plt
import matplotlib.image as mpimg
fig, ax = plt.subplots()

# getting rid of axis
plt.axis('off')

# Reading saved image from folder
img = mpimg.imread(r'img.jpg')

# displaying image
plt.imshow(img)

# Scaling by factor 0.75
plt.colorbar(shrink=0.75)
plt.show()

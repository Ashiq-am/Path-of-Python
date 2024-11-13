# importing library
import matplotlib.pyplot as plt

# Some data to show as an image
data = [[1, 2, 3],
		[4, 5, 6]]

# Call imshow() to display 2-D data as an image
img = plt.imshow(data)

# Scaling colorbar by factor 0.5
plt.colorbar(shrink=0.5)
plt.show()

from matplotlib import image
from matplotlib import pyplot as plt

# to read the image stored in the working directory
data = image.imread('sunset-1404452-640x480.jpg')

# to draw a line from (200,300) to (500,100)
x = [200, 500]
y = [300, 100]
plt.plot(x, y, color="white", linewidth=3)
plt.imshow(data)
plt.show()

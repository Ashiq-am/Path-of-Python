from matplotlib import image
from matplotlib import pyplot as plt

# to read the image stored in the working directory
data = image.imread('sunset-1404452-640x480.jpg')

# to draw first line from (100,400) to (500,100)
# to draw second line from (150,100) to (450,400)
x1 = [100, 500]
y1 = [400, 100]
x2 = [150, 450]
y2 = [100, 400]
plt.plot(x1, y1, x2, y2, color="white", linewidth=3)
plt.axis('off')
plt.imshow(data)
plt.show()

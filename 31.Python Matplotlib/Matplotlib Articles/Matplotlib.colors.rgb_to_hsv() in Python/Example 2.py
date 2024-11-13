import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


image = mpimg.imread('food.jpeg')
plt.title("Output image")


hsv = matplotlib.colors.rgb_to_hsv(image)
plt.imshow(hsv)

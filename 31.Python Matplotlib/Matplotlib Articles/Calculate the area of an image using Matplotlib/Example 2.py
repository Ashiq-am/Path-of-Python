# import necessary library
import matplotlib.pyplot as plt

# read an image
img = plt.imread("image.jpg")

# fetch the height and width
height, width, _ = img.shape

# area is calculated as “height x width”
area = height * width

# display the area
print("Area of the image is : ", area)

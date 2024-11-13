# importing required libraries
import matplotlib.pyplot as plt
import matplotlib.image as img

# reading the image
testImage = img.imread('g4g.png')

# displaying the shape of the image
print(testImage.shape)

# modifying the shape of the image
modifiedImage = testImage[50:200, 100:200, 1]

# displaying the modified image
plt.imshow(modifiedImage)

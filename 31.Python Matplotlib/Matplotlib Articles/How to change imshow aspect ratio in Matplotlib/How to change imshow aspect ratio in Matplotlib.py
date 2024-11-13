import matplotlib.pyplot as plt
import cv2

# reading image from directory
im = cv2.imread("C://Users/User/Downloads/chess5.png")

# plotting a figure for showing all
# images in a single plot
fig = plt.figure(figsize=(4, 4))

# plotting each matplot image with
# different aspect ratio parameter values
# in a seperate subplot
ax1 = fig.add_subplot(2, 2, 1)
ax1.set_xlabel('Original')

# plot the initial image as the first image
plt.imshow(im)

ax2 = fig.add_subplot(2, 2, 2)
ax2.set_xlabel('Aspect Ratio : Auto')

# plot the image with "auto" aspect ratio
# as the second image
plt.imshow(im, aspect='auto')

ax3 = fig.add_subplot(2, 2, 3)
ax3.set_xlabel('Aspect Ratio : 0.5')

# plot the image with "0.5" aspect ratio
# as the third image
plt.imshow(im, aspect='0.5')

ax4 = fig.add_subplot(2, 2, 4)
ax4.set_xlabel('Aspect Ratio : 1.5')

# plot the image with "1.5" aspect ratio
# as the fourth image
plt.imshow(im, aspect='1.5')

# display the plot
plt.show()

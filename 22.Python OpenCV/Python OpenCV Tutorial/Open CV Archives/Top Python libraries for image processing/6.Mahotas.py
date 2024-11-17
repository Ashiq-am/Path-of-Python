import mahotas as mh
import matplotlib.pyplot as plt

# Step 1: Read the image
image = mh.imread('rose.jpg')

# Step 2: Convert the image to sepia tone
output_image = mh.colors.rgb2sepia(image)

# Step 3: Display the sepia-toned image
plt.imshow(output_image)

# Step 4: Show axis
plt.axis('on')

# Step 5: Show the image
plt.show()

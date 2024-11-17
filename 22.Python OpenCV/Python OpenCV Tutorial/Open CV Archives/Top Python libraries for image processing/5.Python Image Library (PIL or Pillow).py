from PIL import Image
image = Image.open('rose.jpg')
box = (500, 500, 2500, 2500)
cropped_image = image.crop(box)
cropped_image.save('cropped_image.jpg')

# Print size of cropped image
print(cropped_image.size)

# Plot the image
plt.imshow(cropped_image)
plt.axis('on') # Turn on axis
plt.show()

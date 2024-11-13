image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image in RGB Mode
plt.imshow(image)
plt.title('Image in RGB Mode')
plt.axis('off')
plt.show()

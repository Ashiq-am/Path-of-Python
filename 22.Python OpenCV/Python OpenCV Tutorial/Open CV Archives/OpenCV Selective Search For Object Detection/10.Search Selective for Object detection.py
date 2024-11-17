# Load the image
image_path = 'elephant.jpg'
image = cv2.imread(image_path)

# Get selective search object proposals
proposals = selective_search(image)

# Draw the proposals on the image
output_image = image.copy()
for (x, y, w, h) in proposals:
	cv2.rectangle(output_image, (x, y), (x + w, y + h), (0, 255, 0), 20)

# Display the result
plt.imshow(output_image)
plt.show()

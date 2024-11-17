# Load the image from the specified path
image_path = 'dog.jpg'
image = cv2.imread(image_path)

# Get region proposals using Selective Search
proposals = selective_search(image)

# Create a copy of the original image to draw bounding boxes on
output_image = image.copy()

# Iterate through each region proposal and draw bounding boxes
for (x, y, w, h) in proposals:
	# Define the coordinates and dimensions of the bounding box
	x1, y1 = x, y # Top-left corner
	x2, y2 = x + w, y + h # Bottom-right corner

	# Draw a green bounding box around the region proposal on the output image
	cv2.rectangle(output_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Display the result image with bounding boxes
plt.imshow(output_image)
plt.show()

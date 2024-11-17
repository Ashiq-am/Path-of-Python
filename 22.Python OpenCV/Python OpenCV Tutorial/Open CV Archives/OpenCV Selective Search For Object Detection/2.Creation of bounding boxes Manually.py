# Load the image
image_path = 'img_1.jpg'
image = cv2.imread(image_path)
# Define bounding box coordinates (x, y, width, height)
bounding_boxes = [
	(100, 50, 200, 150), # Example bounding box 1
	(300, 200, 150, 100), # Example bounding box 2
	# Add more bounding boxes as needed
]

# Draw bounding boxes on the image
for (x, y, w, h) in bounding_boxes:
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with bounding boxes
cv2_imshow(image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

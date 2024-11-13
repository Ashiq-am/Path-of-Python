import cv2

# Path to the image sequence (using %03d to match the pattern img_001.jpg, img_002.jpg, etc.)
image_sequence_path = 'path/to/images/img_%03d.jpg'

# Initialize the VideoCapture object with the image sequence path
cap = cv2.VideoCapture(image_sequence_path)

# Check if the VideoCapture object was successfully created
if not cap.isOpened():
    print("Error: Could not open image sequence.")
    exit()

# Read and display the images in the sequence
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Image Sequence', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the display window
cap.release()
cv2.destroyAllWindows()

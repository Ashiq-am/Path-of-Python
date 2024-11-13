import cv2
import glob

# Path to the image sequence
image_files = sorted(glob.glob('path/to/images/*.jpg'))

for image_file in image_files:
    image = cv2.imread(image_file)
    if image is None:
        print(f"Error: Could not read image {image_file}")
        continue
    cv2.imshow('Image Sequence', image)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

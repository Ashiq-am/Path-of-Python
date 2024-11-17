import cv2

# Load image from local path
image_path = 'C:\\Users\\Asus\\Dropbox\\PC\\Downloads\\gfg-new-logo.png'
image = cv2.imread(image_path)

if image is None:
    raise ValueError("Image not found or unable to load")
print(f"Loaded image shape: {image.shape}")

# import opencv module
import cv2

# load image
image_path = "path_to_image.png"
image = cv2.imread(image_path)

# function to resize image
# maintaing the aspect ratio
def resize_with_aspect_ratio(image, target_size):
    h, w = image.shape[:2]
    scale = min(target_size / h, target_size / w)
    new_w = int(w * scale)
    new_h = int(h * scale)
    resized_image = cv2.resize(image, (new_w, new_h))

    delta_w = target_size - new_w
    delta_h = target_size - new_h
    top, bottom = delta_h // 2, delta_h - (delta_h // 2)
    left, right = delta_w // 2, delta_w - (delta_w // 2)

    color = [0, 0, 0]
    new_image = cv2.copyMakeBorder(
        resized_image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
    return new_image

resized_image = resize_with_aspect_ratio(image, 608)
print(f"Resized image shape: {resized_image.shape}")

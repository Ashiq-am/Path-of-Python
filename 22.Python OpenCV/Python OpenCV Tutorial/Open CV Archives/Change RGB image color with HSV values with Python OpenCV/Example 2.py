import cv2
import numpy as np


def modify_hsv_image(image_path, hue_change=0, saturation_change=0, value_change=0, display_result=True):
    original_img = cv2.imread(image_path)

    if original_img is None:
        raise FileNotFoundError(f"Error: Could not read image from {image_path}")

    # Convert the image from BGR to HSV
    hsv_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2HSV)

    # Apply hue change (wrap around for values outside 0-179)
    hsv_img[..., 0] = (hsv_img[..., 0] + hue_change) % 180

    # Apply saturation and value changes with clipping (0-255)
    hsv_img[..., 1] = np.clip(hsv_img[..., 1] + saturation_change, 0, 255)
    hsv_img[..., 2] = np.clip(hsv_img[..., 2] + value_change, 0, 255)

    bgr_img_new = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)

    if display_result:
        cv2.imshow("Covered_modified_bird Image", bgr_img_new)
        cv2.imwrite('Covered_modified_bird_image.jpg', bgr_img_new)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return bgr_img_new


if __name__ == "__main__":
    img_path = "bird.jpg"
    hue_change = 10
    saturation_change = 15
    value_change = 5
    try:
        modified_image = modify_hsv_image(img_path, hue_change, saturation_change, value_change)
    except FileNotFoundError as e:
        print(e)

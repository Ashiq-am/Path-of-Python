# import opencv module
import cv2

# load image
image_path = "path_to_image.png"
image = cv2.imread(image_path)

# resize image
resized_image = cv2.resize(image, (608, 608))


# function to rotate image
def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    # creating rotation matrix
    M = cv2.getRotationMatrix2D(center, angle, 1.0)

    # applying rotation to the image
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated


rotated_image = rotate_image(resized_image, 45)

# displaying image
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

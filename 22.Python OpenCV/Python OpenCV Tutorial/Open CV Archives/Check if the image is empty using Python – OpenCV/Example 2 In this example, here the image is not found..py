# Importing OpenCV library
import cv2


# user define funtion
# that return None or
def check_empty_img(url):
    # Reading Image
    # You can give path to the
    # image as first argument
    image = cv2.imread(url)

    # Checking if the image is empty or not
    if image is None:
        result = "Image is empty!!"
    else:
        result = "Image is not empty!!"

    return result


# driver node
img = "geek.png"

# Calling and printing
# the funtion
print(check_empty_img(img))

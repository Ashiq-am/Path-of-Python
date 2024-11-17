# Importing OpenCV
import cv2

# Path to image [NOTE: Here resized image
# is used to be able to fit to screen]
path = 'download3.png'

# Reading an image in default mode
image = cv2.imread(path)

# Creating a full screen window with
# name "Display2" using WINDOW_FULLSCREEN
# or WINDOW_NORMAL
cv2.namedWindow("Display2", cv2.WINDOW_NORMAL)

# Using getWindowImageRect()
print(cv2.getWindowImageRect("Display2"))

# Assigning the returned values to variables
(x, y, windowWidth, windowHeight) = cv2.getWindowImageRect("Display2")

print("Origin Coordinates(x,y): ", x, y)
print("Width: ", windowWidth)
print("Height: ", windowHeight)

# Displaying the image using imshow
cv2.imshow('Display2', image)

# Waiting 0ms for user to press any key
cv2.waitKey(0)

# Destroying all created windows
# open on screen
cv2.destroyAllWindows()

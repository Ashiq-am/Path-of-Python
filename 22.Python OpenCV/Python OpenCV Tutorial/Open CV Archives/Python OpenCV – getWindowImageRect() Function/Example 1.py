# Importing OpenCV
import cv2

# Path to image
path = 'C:/Users/Amisha Kirti/Downloads/GFG.png'

# Reading an image in default mode
image = cv2.imread(path)

# Creating window with name "Display1"
# of default size
cv2.namedWindow("Display1", cv2.WINDOW_AUTOSIZE)

# Using getWindowImageRect()
print(cv2.getWindowImageRect("Display1"))

# Assigning the returned values to variables
(x, y, windowWidth, windowHeight) = cv2.getWindowImageRect("Display1")

"""
We can also assign values to variables by
accessing returned value by index

x = cv2.getWindowImageRect("Display1")[0]
y = cv2.getWindowImageRect("Display1")[1]
windowWidth=cv2.getWindowImageRect("Display1")[2]
windowHeight=cv2.getWindowImageRect("Display1")[3]
"""

print("Origin Coordinates(x,y): ", x, y)
print("Width: ", windowWidth)
print("Height: ", windowHeight)

# Displaying the image using imshow
cv2.imshow('Display1', image)

# Waiting 0ms for user to press any key
cv2.waitKey(0)

# Destroying all windows open on screen
cv2.destroyAllWindows()

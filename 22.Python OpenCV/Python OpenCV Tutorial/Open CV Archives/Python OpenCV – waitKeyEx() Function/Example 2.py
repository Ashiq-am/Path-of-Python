# importing cv2 module
import cv2

# read the image
img = cv2.imread("gfg_logo.png")

# showing the image
cv2.imshow('gfg', img)

# waiting using waitKeyEX method and
# storing the returned value in full_key_code
full_key_code = cv2.waitKeyEx(5000)

# printing the variable
print("The key code is:"+str(full_key_code))

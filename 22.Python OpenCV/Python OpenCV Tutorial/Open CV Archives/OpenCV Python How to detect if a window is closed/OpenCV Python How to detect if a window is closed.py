# importing packages
import cv2

# reading image
img = cv2.imread('sunset.jpeg')
cv2.imshow('sunset', img)
while True:

    # it waits till we press a key
    key = cv2.waitKey(0)

    # if we press esc
    if key == 27:
        print('esc is pressed closing all windows')
        cv2.destroyAllWindows()
        break

if cv2.getWindowProperty('sunset', cv2.WND_PROP_VISIBLE) < 1:
    print("ALL WINDOWS ARE CLOSED")
cv2.waitKey(1)

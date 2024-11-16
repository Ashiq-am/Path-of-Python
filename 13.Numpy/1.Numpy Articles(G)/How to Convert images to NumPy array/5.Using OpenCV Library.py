import cv2

image = cv2.imread('Sample.png')

# BGR -> RGB
img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cv2.imwrite('opncv_sample.png', img)
print (type(img))

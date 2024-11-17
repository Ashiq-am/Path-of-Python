import cv2
import numpy as np

img = cv2.imread('naruto.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# dimension of gray image is in 2D
dimensions = gray.shape # (height,weight)

print("Image Dimensions:", dimensions)
n = int(input("Enter the size of the original image to be captured:"))
print("The matrix of the original image:")


for i in range(0, n):
	for j in range(0, n):
		print(gray[i][j], end=" ")
	print()
"""
Apply below filter on image matrix
0 -1 0
-1 4 -1
0 -1 0
"""
filter = np.zeros(shape=(n, n))
for i in range(0, n):
	for j in range(0, n):
		filter[i][j] = 0*gray[i][j]-1*gray[i][j+1]\
		+0*gray[i][j+2]-1*gray[i+1][j]+4 * \
			gray[i+1][j+1]-1*gray[i+1][j+2]+0*gray[i+2][j] - \
			1*gray[i+2][j+1]+0*gray[i+2][j+2]

print("\n")
print("The matrix form after HPF masking the captured image is:")
print("\n")
for hpf in filter:
	print(hpf)

cv2.imshow("Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

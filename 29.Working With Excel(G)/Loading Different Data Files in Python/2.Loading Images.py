import matplotlib.pyplot as plt
import cv2
try:
    image = cv2.imread('download3.png')
    if image is not None:
        plt.figure(figsize=(18, 18))
        plt.imshow(image)
        plt.show()
    else:
        print("Error! Something went wrong!")

except Exception as e:
    print("OOps! Error!", e)

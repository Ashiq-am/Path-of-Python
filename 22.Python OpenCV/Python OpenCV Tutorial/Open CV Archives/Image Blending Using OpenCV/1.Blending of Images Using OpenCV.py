import cv2
import matplotlib.pyplot as plt
import requests
from PIL import Image
from io import BytesIO
import numpy as np

# Image URLs
image1_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmKTFI_7r2TKR0sknfK_7GJX8sHItxbf-zh_jOJIBde2-L69K29IAzFLrD&s"
image2_url = "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQLVI5oqw867VkKFwDFtPaTGx2iRyLI2xth6m96yXdszR9vcfGi"

response_image1 = requests.get(image1_url)
response_image2 = requests.get(image2_url)
img1 = Image.open(BytesIO(response_image1.content))
img2 = Image.open(BytesIO(response_image2.content))

image1 = cv2.cvtColor(np.array(img1), cv2.COLOR_RGB2BGR)
image2 = cv2.cvtColor(np.array(img2), cv2.COLOR_RGB2BGR)

image1 = cv2.resize(image1, (500, 500))
image2 = cv2.resize(image2, (500, 500))

# Set blending weights
alpha = 0.5
beta = 0.5

blended_image = cv2.addWeighted(image1, alpha, image2, beta, 0)
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title('Image 1')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title('Image 2')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(blended_image, cv2.COLOR_BGR2RGB))
plt.title('Blended Image')
plt.axis('off')

plt.show()
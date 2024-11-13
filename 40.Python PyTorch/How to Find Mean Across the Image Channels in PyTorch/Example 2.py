# import required libraries
import torch
import cv2
import torchvision.transforms as transforms

# Read input image using OpenCV
img = cv2.imread('Maximum subarray sum modulo m output.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# create a transform
transform = transforms.ToTensor()

# convert the image to PyTorch Tensor
imgTensor = transform(img)

# Compute the mean of Image across the
# channels RGB
r, g, b = torch.mean(imgTensor, dim=[1, 2])

# Display Result
print("\n\nMean for Red channel: ", r)
print("Mean for Green channel: ", g)
print("Mean for Blue channel: ", b)

# Import required libraries
import torch
import cv2
import torchvision.transforms as transforms

# Read the image
image = cv2.imread('iceland.jpg')

# Convert BGR image to RGB image
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define a transform to convert
# the image to torch tensor
transform = transforms.Compose([
	transforms.ToTensor()
])

# Convert the image to Torch tensor
tensor = transform(image)

# print the converted image tensor
print(tensor)

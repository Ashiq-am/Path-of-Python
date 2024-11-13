import torch

# Create a sample grayscale image tensor with shape (1, H, W)
image_tensor = torch.rand(1, 100, 100)  # Example of a single-channel image tensor

# Check if image_tensor is a grayscale image and has a single channel
if image_tensor.shape[0] == 1:  # Check if single channel
    image_tensor = image_tensor.squeeze(0)  # Remove the channel dimension

print("Shape after squeezing:", image_tensor.shape)

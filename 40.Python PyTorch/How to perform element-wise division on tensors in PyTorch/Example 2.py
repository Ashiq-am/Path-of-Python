# Python program to divide two
# 2D tensors element-wise
# importing torch
import torch

# defining first 2D tensor
a = torch. tensor([[-1.8665, 0.6341, 0.8920],
				[-0.1712, 0.3949, 1.9414],
				[-1.2088, -1.0375, -1.3087],
				[0.9161, -0.2972, 1.5289]])
print("Tensor a:\n", a)

# defining second 2D tensor
# b = torch.randn(4,3)
b = torch. tensor([[-0.2187, 0.5252, -0.5840],
				[1.5293, -0.4514, 1.8490],
				[-0.7269, -0.1561, -0.0629],
				[-0.5379, -0.9751, 0.6541]])
print("\nTensor b:\n", b)

# computing element-wise division
print("\nElement-wise Division:")
result1 = torch.div(a, b)
print("\nResult:\n", result1)
result2 = torch.div(a, b, rounding_mode='trunc')
print("\nResult with rounding_mode='trunc':\n", result2)
result3 = torch.div(a, b, rounding_mode='floor')
print("\nResult with rounding_mode='floor':\n", result3)

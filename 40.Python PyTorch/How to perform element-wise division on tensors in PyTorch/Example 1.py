# Python program to divide two 1D tensors
# element-wise using torch.div() method
# importing torch
import torch

# creating first tensor
A = torch.tensor([0.0312, 0.3401, 0.1645, -1.0781])
print("Tensor A:\n", A)

# creating second tensor
B = torch.tensor([-1.8584, 0.5706, -0.8994, 2.2492])
print("\nTensor B:\n", B)

# divide A by B
result = torch.div(A, B)
print("\nElement-wise Division Output:\n", result)

# Python 3 program to demonstrate torch.stack() method
# for three one-dimensional tensors
# importing torch
import torch

# creating tensors
x = torch.tensor([1., 3., 6., 10.])
y = torch.tensor([2., 7., 9., 13.])
z = torch.tensor([4., 5., 8., 11.])

# printing above created tensors
print("Tensor x:", x)
print("Tensor y:", y)
print("Tensor z:", z)

# join above tensor using "torch.stack()"
print("join tensors:")
t = torch.stack((x, y, z))
# print final tensor after join
print(t)

print("join tensors dimension 0:")
t = torch.stack((x, y, z), dim=0)
print(t)

print("join tensors dimension 1:")
t = torch.stack((x, y, z), dim=1)
print(t)

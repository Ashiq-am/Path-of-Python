# Python 3 program to demonstrate torch.stack() method
# for two 2D tensors.
# importing torch
import torch

# creating tensors
x = torch.tensor([[1., 3., 6.], [10., 13., 20.]])
y = torch.tensor([[2., 7., 9.], [14., 21., 34.]])

# printing above created tensors
print("Tensor x:\n", x)
print("Tensor y:\n", y)

# join above tensor using "torch.stack()"
print("join tensors")
t = torch.stack((x, y))

# print final tensor after join
print(t)

print("join tensors in dimension 0:")
t = torch.stack((x, y), 0)
print(t)

print("join tensors in dimension 1:")
t = torch.stack((x, y), 1)
print(t)
print("join tensors in dimension 2:")
t = torch.stack((x, y), 2)
print(t)

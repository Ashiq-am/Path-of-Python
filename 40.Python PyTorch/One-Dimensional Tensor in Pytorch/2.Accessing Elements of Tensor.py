# importing torch module
import torch

# create one dimensional tensor with integer type elements
a = torch.tensor([10, 20, 30, 40, 50])

# get 0 and 1 index elements
print(a[0], a[1])

# get 4 th index element
print(a[4])

# get 4 index element from last
print(a[-4])

# get 2 index element from last
print(a[-2])

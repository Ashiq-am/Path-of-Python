# import torch
import torch


# create a tensor with unsigned integer type of 8 bytes size
a = torch.tensor([100, 200, 2, 3, 4], dtype=torch.uint8)
# display tensor
print(a)
# display data type
print(a.dtype)

# create a tensor with integer type of 8 bytes size
a = torch.tensor([1, 2, -6, -8, 0], dtype=torch.int8)

# display tensor
print(a)

# display data type
print(a.dtype)

# create a tensor with integer type of 16 bytes size
a = torch.tensor([1, 2, -6, -8, 0], dtype=torch.int16)

# display tensor
print(a)

# display data type
print(a.dtype)


# create a tensor with integer type of 32 bytes size
a = torch.tensor([1, 2, -6, -8, 0], dtype=torch.int32)

# display tensor
print(a)

# display data type
print(a.dtype)

# create a tensor with integer type of 64 bytes size
a = torch.tensor([1, 2, -6, -8, 0], dtype=torch.int64)

# display tensor
print(a)

# display data type
print(a.dtype)

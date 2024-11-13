# import torch library
import torch

# define tensor
tens = torch.Tensor([5.344, 8.343, -2.398, -0.995, 5, 30.421])
print("Original tensor: ", tens)

# find top 2 elements
values, indexes = torch.topk(tens, 2)

# print top 2 elements
print("Top 2 element values:", values)


# print index of top 2 elements
print("Top 2 element indices:", indexes)

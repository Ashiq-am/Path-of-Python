# import library
import torch

# create two 2D tensors
first = torch.Tensor([[7, -2, 3],
					[29, 9, -5],
					[2, -8, 34],
					[24, 62, 98]])

second = torch.Tensor([[7, -5, 3],
					[26, 9, -4],
					[3, -8, 43],
					[23, -62, 98]])

# print first tensors
print("First Tensor:", first)

# print second tensors
print("Second Tensor:\n", second)


print("After Comparing Both Tensors")

# Compare element wise tensors first
# and second
print(torch.eq(first, second))

import torch

# first argument 1D and second argument 2D
mat1_1 = torch.tensor([3, 6, 2])

mat1_2 = torch.tensor([[1, 2, 3],
					[4, 3, 8],
					[1, 7, 2]])

out_1 = torch.matmul(mat1_1, mat1_2)
print("\n1D-2D multiplication :\n", out_1)

# first argument 2D and second argument 1D
mat2_1 = torch.tensor([[2, 4, 1],
					[1, 3, 6],
					[2, 6, 5]])

mat2_2 = torch.tensor([4, 1, 9])

# assigning to output tensor
out_2 = torch.matmul(mat2_1, mat2_2)

print("\n2D-1D multiplication :\n", out_2)

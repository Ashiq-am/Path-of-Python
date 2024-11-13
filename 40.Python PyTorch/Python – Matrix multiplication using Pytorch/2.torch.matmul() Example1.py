import torch as t

# both arguments 1D
vec_1 = torch.tensor([3, 6, 2])
vec_2 = torch.tensor([4, 1, 9])

print("Single dimensional tensors :", torch.matmul(vec_1, vec_2))

# both arguments 2D
mat_1 = torch.tensor([[1, 2, 3],
					[4, 3, 8],
					[1, 7, 2]])

mat_2 = torch.tensor([[2, 4, 1],
					[1, 3, 6],
					[2, 6, 5]])

out = torch.matmul(mat_1, mat_2)

print("\n3x3 dimensional tensors :\n", out)

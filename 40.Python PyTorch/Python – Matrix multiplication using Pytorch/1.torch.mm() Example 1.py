import torch as t

mat_1 = torch.tensor([[1, 2, 3],
					[4, 3, 8],
					[1, 7, 2]])

mat_2 = torch.tensor([[2, 4, 1],
					[1, 3, 6],
					[2, 6, 5]])

torch.mm(mat_1, mat_2, out=None)

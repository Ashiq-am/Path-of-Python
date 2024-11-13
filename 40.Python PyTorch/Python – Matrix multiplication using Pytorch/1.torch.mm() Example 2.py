import torch as t

mat_1 = torch.tensor([[1, 2],
					[4, 3]])

mat_2 = torch.tensor([[2, 4, 1],
					[1, 3, 6]])

torch.mm(mat_1, mat_2, out=None)

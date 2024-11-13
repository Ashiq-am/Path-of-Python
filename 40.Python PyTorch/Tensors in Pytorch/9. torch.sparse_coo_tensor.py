i = [[0, 1, 1],
	[2, 0, 2]]

v = [3, 4, 5]
s = torch.sparse_coo_tensor(i, v, (2, 3))
Print(s)

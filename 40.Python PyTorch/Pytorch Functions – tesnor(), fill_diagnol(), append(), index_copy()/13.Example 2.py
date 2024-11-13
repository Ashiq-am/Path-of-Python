a = torch.tensor([[1, 8], [9, 5], [1, 5]])

b = torch.tensor([[3, 5], [9, 0], [2, 2]])

i = torch.tensor([2, 1, 0])

a.index_copy_(0, i, b)

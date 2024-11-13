a = torch.tensor([[8, 3], [1, 0]])

b = torch.tensor([[3, 9]])

i = torch.tensor([1])

a.index_copy(1, i, b)

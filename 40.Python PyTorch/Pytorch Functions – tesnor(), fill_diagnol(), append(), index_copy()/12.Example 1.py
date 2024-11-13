self_tensor = torch.zeros(6, 3)

a

t = torch.tensor([[7, 6, 9], [3, 9, 1], [0, 1, 9]], dtype = torch.float)

i = torch.tensor([3, 1, 0])

self_tensor.index_copy_(0, i, t)

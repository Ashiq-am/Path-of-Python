b = torch.zeros([9, 4])

# without putting wrap = True

A = b.fill_diagonal_(5, wrap = False)

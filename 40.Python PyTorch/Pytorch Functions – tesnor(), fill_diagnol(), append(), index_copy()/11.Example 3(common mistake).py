c = torch.tensor([[4, 6], [9, 6]])

c.size() # this matrix didn't any singleton dimemsion

c.expand(2, 6)

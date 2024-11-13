input = torch.tensor([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
index = torch.tensor([[0, 1], [1, 2], [2, 0]])
output = torch.gather(input, 1, index)
print(output)

import torch

data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
reshaped_data = torch.reshape(data, (4, 2))
print(reshaped_data)

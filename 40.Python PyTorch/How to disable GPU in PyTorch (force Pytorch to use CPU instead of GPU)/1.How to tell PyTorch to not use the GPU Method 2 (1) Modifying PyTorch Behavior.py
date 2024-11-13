import torch

device = torch.device("cpu")
mytensor = torch.rand(5,5, device=device)
print(mytensor)

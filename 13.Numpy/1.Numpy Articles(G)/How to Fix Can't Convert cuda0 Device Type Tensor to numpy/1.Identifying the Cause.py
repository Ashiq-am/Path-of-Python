import torch

tensor = torch.tensor([1, 2, 3], device='cuda:0')
numpy_array = tensor.numpy()  # This will raise the error

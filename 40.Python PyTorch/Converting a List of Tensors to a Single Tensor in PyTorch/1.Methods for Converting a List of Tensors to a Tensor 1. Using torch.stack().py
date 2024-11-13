import torch

tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([4, 5, 6])
tensor3 = torch.tensor([7, 8, 9])

# List of tensors
tensor_list = [tensor1, tensor2, tensor3]

# Stack tensors along a new dimension
stacked_tensor = torch.stack(tensor_list, dim=0)
print(stacked_tensor)

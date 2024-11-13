import torch

# Example tensors
tensor1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
tensor2 = torch.tensor([[7, 8, 9], [10, 11, 12]])

# List of tensors
tensor_list = [tensor1, tensor2]

# Concatenate tensors along dimension 0
concatenated_tensor = torch.cat(tensor_list, dim=0)
print(concatenated_tensor)

import torch

# Example tensors with different data types
tensor1 = torch.tensor([1, 2, 3], dtype=torch.float32)
tensor2 = torch.tensor([4, 5, 6], dtype=torch.int32)

# Convert tensors to the same data type
tensor2 = tensor2.to(dtype=torch.float32)

# Stack tensors
stacked_tensor = torch.stack([tensor1, tensor2], dim=0)
print(stacked_tensor)

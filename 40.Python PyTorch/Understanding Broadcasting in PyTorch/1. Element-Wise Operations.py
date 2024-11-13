import torch

A = torch.tensor([[1, 2, 3], [4, 5, 6]])  # Shape (2, 3)
B = torch.tensor([10, 20, 30])           # Shape (3,)

result = A + B  # Broadcasting B to shape (2, 3)

print("\nResult of a + b (after broadcasting):")
print(result)

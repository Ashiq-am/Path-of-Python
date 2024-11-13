import torch

# Define two tensors with different shapes
A = torch.tensor([[1, 2, 3], [4, 5, 6]])  # Shape (2, 3)
B = torch.tensor([10, 20, 30])            # Shape (3,)

# Perform element-wise addition with broadcasting
result = A + B  # B is broadcasted to match the shape of A (2, 3)

print("Tensor A:")
print(A)
print("\nTensor B:")
print(B)
print("\nResult of A + B (with broadcasting):")
print(result)

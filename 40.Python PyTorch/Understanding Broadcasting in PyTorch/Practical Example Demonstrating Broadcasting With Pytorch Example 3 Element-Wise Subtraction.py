import torch

# Define a 3D tensor and a 1D tensor
A = torch.tensor([[[1, 2, 3],
                   [4, 5, 6]],

                  [[7, 8, 9],
                   [10, 11, 12]]])  # Shape (2, 2, 3)

B = torch.tensor([1, 2, 3])  # Shape (3,)

# Perform element-wise subtraction with broadcasting
result = A - B  # B is broadcasted to match the last dimension of A

print("Tensor A:")
print(A)
print("\nTensor B:")
print(B)
print("\nResult of A - B (with broadcasting):")
print(result)

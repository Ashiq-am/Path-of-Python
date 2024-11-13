import torch

# Create a tensor from a list
tensor1 = torch.tensor([1, 2, 3])
print("Tensor from list:", tensor1)

# Create a tensor of zeros with shape (2, 3)
tensor2 = torch.zeros(2, 3)
print("Tensor of zeros:", tensor2)

# Create a random tensor with shape (3, 2)
tensor3 = torch.rand(3, 2)
print("Random tensor:", tensor3)

# Performing operations on Tensors

# Addition
result_add = tensor1 + tensor2
print("Addition result:", result_add)


# Multiplication
result_mul = tensor2 * 5
print("Multiplication result:", result_mul)


# Matrix multiplication
result_matmul = torch.matmul(tensor2, tensor3)
print("Matrix multiplication result:", result_matmul)

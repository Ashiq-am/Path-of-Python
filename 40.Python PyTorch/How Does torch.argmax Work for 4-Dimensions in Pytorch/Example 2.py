# import necessary libraries
import torch

# define a random 4D tensor
A = torch.randn(1, 2, 3, 4)
print("Tensor-A:", A)
print(A.shape)

# use argmax method on 4d tensor along axis-2
print('---Output tensor along axis-2---')
print(torch.argmax(A, axis=2, keepdims=True))
print(torch.argmax(A, axis=2, keepdims=True).shape)

# use argmax method on 4d tensor along axis-3
print('---Output tensor along axis-3---')
print(torch.argmax(A, axis=3, keepdims=True))
print(torch.argmax(A, axis=3, keepdims=True).shape)

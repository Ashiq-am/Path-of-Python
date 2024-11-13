# import necessary libraries
import torch

# define a random 4D tensor
A = torch.randn(1, 2, 3, 4)
print("Tensor-A:", A)
print(A.shape)

# use argmax method on 4d tensor along axis-0
print('---Output tensor along axis-0---')
print(torch.argmax(A, axis=0, keepdims=False))
print(torch.argmax(A, axis=0, keepdims=False).shape)

# use argmax method on 4d tensor along axis-2
print('---Output tensor along axis-2---')
print(torch.argmax(A, axis=2))
print(torch.argmax(A, axis=2).shape)

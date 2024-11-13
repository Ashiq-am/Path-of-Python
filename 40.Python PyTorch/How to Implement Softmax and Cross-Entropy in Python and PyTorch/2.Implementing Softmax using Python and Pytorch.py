# The below code implements the softmax function
# using the function softmax provided by
# torch.nn.functional in pytorch.
# Input: The input values (list, array)
# Output: List (Computed softmax values)


# Importing the required Libraries
import torch.nn.functional as F
import torch

# The input tensor to be passed
input_ = torch.tensor([1, 2, 3])

# Printing the loss value
softmax = F.softmax(input_.float(), dim=0)
print("Softmax values are: ", softmax)

# Sum of all the softmax values
print("Sum of the softmax values: ", torch.sum(softmax))

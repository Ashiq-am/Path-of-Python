import torch

# this function will make a
# tensor of 5X5 array with
# random numbers
rand_matrix = torch.rand(5, 5)

print(rand_matrix)

# Bernoulli distribution
# this function will do the bernoulli
# distrobution on the given matrix and
# form the new tensor
torch.bernoulli(rand_matrix)

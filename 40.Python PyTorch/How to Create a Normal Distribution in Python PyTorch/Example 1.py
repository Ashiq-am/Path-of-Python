# import the torch module
import torch

# create the mean with 5 values
mean = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# create the standard deviation with 5 values
std = torch.tensor([1.22, 0.78, 0.56, 1.23, 0.23])

# create normal distribution
print(torch.normal(mean, std))

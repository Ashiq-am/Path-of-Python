# import the torch module
import torch

# create the mean with single value
mean = torch.tensor(3.4)

# create the standard deviation with
# single value
std = torch.tensor(4.2)

# create normal distribution
print(torch.normal(mean, std))

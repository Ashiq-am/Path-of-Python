import torch
from torch.distributions import Normal
from torch.distributions.kl import kl_divergence

# Define two Gaussian distributions
p = Normal(torch.tensor([0.0]), torch.tensor([1.0]))
q = Normal(torch.tensor([1.0]), torch.tensor([1.5]))

# Compute KL divergence
kl_div = kl_divergence(p, q)
print(kl_div)

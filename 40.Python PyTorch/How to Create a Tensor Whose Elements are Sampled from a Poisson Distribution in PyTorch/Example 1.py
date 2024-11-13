# import required libraries
import torch

# create torch tensor of rate parameters
rates_tens = torch.tensor([2.7345, 3.4347,
						4.1237, 1.3379, 3.2343])
print("tensor of rate parameters: ", rates_tens)

# apply possion() method
pois_tens = torch.poisson(rates_tens)

# display result
print("Poisson Tensor: ", pois_tens)

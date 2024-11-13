# import required libraries
import torch

# create torch tensor of rate parameters
rates_tens = torch.tensor([[4.1237, 1.8373, 3.2343],
						[2.3344, 3.3324, 1.3378],
						[3.2349, 2.4447, 4.5269]])

print("tensor of rate parameters: \n", rates_tens)

# apply possion() method
pois_tens = torch.poisson(rates_tens)

# display result
print("Poisson Tensor: \n", pois_tens)

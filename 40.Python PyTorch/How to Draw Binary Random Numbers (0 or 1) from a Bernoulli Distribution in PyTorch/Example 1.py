# Import required library
import torch

# create a tensor containing the
# probability of drawing 1.
tens = torch.tensor([0.1498, 0.9845, 0.4578,
					0.3495, 0.2442])
print(" Input tensor: ", tens)

# Draw random numbers (0,1)
random_num = torch.bernoulli(tens)

# display result
print(" Output tensor ", random_num)

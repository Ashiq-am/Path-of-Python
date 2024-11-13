# Import required library
import torch

# create a tensor containing the
# probability of drawing 1.
tens = torch.tensor([[0.2432, 0.7579, 0.6325],
					[0.3464, 0.2442, 0.3847],
					[0.4528, 0.9876, 0.8499], ])
print("\n Input tensor: \n", tens)

# Draw random numbers (0,1)
random_num = torch.bernoulli(tens)

# display result
print("\n Output tensor \n", random_num)

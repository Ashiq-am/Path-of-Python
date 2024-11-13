import torch

# define first vector
vec1 = torch.tensor([[0.2245, 0.2959, 0.3597, 0.6766],
					[0.3685, 0.6469, 0.3765, 0.7898],
					[0.4577, 0.3228, 0.4699, 0.2389]])

# define second vector
vec2 = torch.tensor([[0.2423, 0.4667, 0.4434, 0.3598],
					[0.2956, 0.6932, 0.5387, 0.2245],
					[0.8277, 0.2597, 0.9834, 0.9987]])

# display tensors
print("\n First Vector: \n", vec1)
print("\n Second Vector: \n", vec2)

# define an instance of the PairwiseDistance
pdist = torch.nn.PairwiseDistance(p=2)

# compute the pairwise distance
result = pdist(vec1, vec2)

# display result
print("\n Pairwise Distance: \n", result)

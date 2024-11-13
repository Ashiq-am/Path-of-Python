import torch

# define first vector
vec1 = torch.tensor([1., 2., 3., 4.])

# define second vector
vec2 = torch.tensor([5., 6., 7., 8.])

# display tensors
print("\n First Vector: ", vec1)
print("\n Second Vector: ", vec2)

# define an instance of the PairwiseDistance
pdist = torch.nn.PairwiseDistance(p=2)

# compute the pairwise distance
result = pdist(vec1, vec2)

# display result
print("\n Pairwise Distance:", result)

# Import required library
import torch

# define two 1D tensors
tens_1 = torch.tensor([0.5, 0.3, 1.2, 0.33])
tens_2 = torch.tensor([0.3, 0.2, 1.3, 1.4])

# print above defined two tensors
print("\n First Tensor: ", tens_1)
print("\n Second Tensor: ", tens_2)

# compute cosine similarity
cosi = torch.nn.CosineSimilarity(dim=0)
output = cosi(tens_1, tens_2)

# display the output tensor
print("\n Computed Cosine Similarity: ", output)

# Import required library
import torch

# define first 2D tensor
tens_1 = torch.tensor([[0.2245, 0.2959,
						0.3597, 0.6766],
					[-2.2268, 0.6469,
						0.3765, 0.7898],
					[0.4577, 0.3228,
						0.4699, 0.2389]])

# define second 2D tensor
tens_2 = torch.tensor([[0.2423, 0.4667,
						0.4434, 0.3598],
					[-0.6679, 0.6932,
						0.5387, 0.2245],
					[0.8277, 0.2597,
						0.9834, 0.9987]])

# print above defined two tensors
print("\n\n First Tensor: \n", tens_1)
print("\n Second Tensor: \n", tens_2)

# compute cosine similarity in dim=0
cos_1 = torch.nn.CosineSimilarity(dim=0)
output_1 = cos_1(tens_1, tens_2)

# display the output tensor
print("\n\nComputed Cosine Similarity in dim=0: ",
	output_1)


# compute cosine similarity in dim=1
cos_2 = torch.nn.CosineSimilarity(dim=1)
output_2 = cos_2(tens_1, tens_2)

# display the output tensor
print("\n\nComputed Cosine Similarity in dim=1: ",
	output_2)

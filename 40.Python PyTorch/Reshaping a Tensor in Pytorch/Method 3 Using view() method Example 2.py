# importing torch module
import torch

# create one dimensional tensor 10 elements
a = torch.FloatTensor([24, 56, 10, 20, 30,
					40, 50, 1, 2, 3])

# view tensor in 10 rows and 1 column
print(a.view(10, 1))

# view tensor in 1 row and 10 columns
print(a.view(1, 10))

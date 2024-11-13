# importing torch module
import torch

# create one dimensional tensor 12 elements
a=torch.FloatTensor([24, 56, 10, 20, 30,
					40, 50, 1, 2, 3, 4, 5])

# view tensor in 4 rows and 3 columns
print(a.view(4, 3))

# view tensor in 3 rows and 4 columns
print(a.view(3, 4))

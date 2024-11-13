# importing torch module
import torch

# create one dimensional tensor
# 10 elements
a = torch.FloatTensor([10, 20, 30, 40, 50, 1, 2, 3, 4, 5])

# view tensor in 5 rows and 2
# columns
print(a.view(5, 2))

# view tensor in 2 rows and 5
# columns
print(a.view(2, 5))

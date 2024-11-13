# import required libraries
import torch

# creating a 1D tensor
tens = torch.tensor([-0.7336, -0.9200, -0.4742,
					-0.4470, -0.3472])

# print above created tensor
print("\n Input Tensor:", tens)

# compute the error function
er = torch.special.erf(tens)

# Display result
print("\n After Computed Error function :", er)

# import required libraries
import torch

# creating a batch of tensor
tens = torch.tensor([[[0.8636, -0.4195, -0.4681],
					[0.1265, 1.2233, 0.1978],
					[1.1389, 0.3686, 1.2339]],
					[[1.6362, 0.6235, 1.2631],
					[0.3336, 1.5336, 1.3677],
					[0.5637, 1.3236, 0.2696]]])

# print above created tensor
print("\n\n Input Tensor: \n", tens)

# compute the error function
er = torch.special.erf(tens)

# Display result
print("\n\n After Computed Error function: \n", er)

# import the required library
import torch

# define a tensor (matrix)
M = torch.tensor([[-0.1345, -0.7437, 1.2377],
				[0.9337, 1.6473, 0.4346],
				[-1.6345, 0.9344, -0.2456]])

# display input tensor
print("\n Input Matrix M: \n", M)

print("When P is fro = ", torch.linalg.cond(M, p='fro'))
print("When P is nuc =", torch.linalg.cond(M, p='nuc'))
print("When P is inf =", torch.linalg.cond(M, p=float('inf')))
print("When P is -inf =", torch.linalg.cond(M, p=float('-inf')))
print("When P is 1 =", torch.linalg.cond(M, p=1))
print("When P is -1 =", torch.linalg.cond(M, p=-1))
print("When P is 2 =", torch.linalg.cond(M, p=2))
print("When P is -2 =", torch.linalg.cond(M, p=-2))

import torch
import torch.nn as nn

class Softplus(nn.Module):
	def __init__(self):
		super(Softplus, self).__init__()

	def forward(self, x, beta=1):
		return 1/beta * torch.log(1 + torch.exp(beta * x))

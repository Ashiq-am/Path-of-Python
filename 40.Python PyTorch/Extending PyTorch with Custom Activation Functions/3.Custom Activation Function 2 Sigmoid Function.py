import torch
import torch.nn as nn

class sigmoid(nn.Module):
	def __init__(self):
		super(sigmoid, self).__init__()

	def forward(self, x):
		return 1/(1 + torch.exp(-x))

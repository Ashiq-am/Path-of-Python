import torch
import torch.nn as nn

class CustomLayer(nn.Module):
  def __init__(self,ip_size):
    super().__init__()
    self.size = ip_size
    weight_tensor = torch.Tensor(self.size)
    self.weight = nn.Parameter(weight_tensor)
    torch.nn.init.normal_(self.weight,mean=0.0,std=1.0)

  def forward(self,x):
    return x * self.weight

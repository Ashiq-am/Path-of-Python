import torch
# Create a tensor on the CPU
tensor = torch.randn((3, 3))
#Move the tensor to the GPU
tensor = tensor.to('cuda')

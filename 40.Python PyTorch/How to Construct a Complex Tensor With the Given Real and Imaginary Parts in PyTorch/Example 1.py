# import the torch module
import torch

# create real and img with float type
real = torch.tensor([78.2, 23.2], dtype=torch.float32)
img = torch.tensor([32, 41], dtype=torch.float32)

# display
print(real)
print(img)

# display the complex number
print(torch.complex(real, img))

# display the datatype of complex number
print(torch.complex(real, img).dtype)

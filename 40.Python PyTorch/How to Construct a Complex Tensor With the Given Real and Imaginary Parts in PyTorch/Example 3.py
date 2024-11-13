# import the torch module
import torch

# create real and img with double type
real = torch.tensor([78, 23, 45], dtype=torch.float64)
img = torch.tensor([32, 41, 9], dtype=torch.double)

# display
print(real)
print(img)

# display the complex number
print(torch.complex(real, img))

# display the datatype of complex number
print(torch.complex(real, img).dtype)

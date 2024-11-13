#import pytorch
import torch

#import numpy
import numpy as np

#import matplotlib
import matplotlib.pyplot as plt

# create lin space from 1 to 12
x = torch.linspace(1, 12)

# sin function
y = torch.sin(x)

# plot
plt.plot(x.numpy(), y.numpy())

# display
plt.show()

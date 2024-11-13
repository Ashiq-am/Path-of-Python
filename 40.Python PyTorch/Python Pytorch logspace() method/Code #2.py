# Importing the PyTorch library
import torch
# Importing the NumPy library
import numpy as np

# Importing the matplotlib.pylot function
import matplotlib.pyplot as plt

# Applying the logspace function to get a tensor of size 15 with values from -5 to 5 using base 2
a = torch.logspace(-5, 5, 15, 2)
print(a)

# Plotting
plt.plot(a.numpy(), np.zeros(a.numpy().shape), color = 'red', marker = "o")
plt.title("torch.linspace")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()

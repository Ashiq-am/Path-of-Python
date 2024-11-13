# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Create a 2x2 grid of plots
fig, axes = plt.subplots(2, 2, constrained_layout=True)
a = np.linspace(0, 1)

# Modify top-left plot
axes[0,0].set_title("Top--Left", color="g")
axes[0,0].plot(x, x)

# Modify top-right plot
axes[0,1].set_title("Top--Right", color="r")
axes[0,1].plot(x, x**2)

# Modify bottom-left plot
axes[1,0].set_title("Bottom--Left", color="b")
axes[1,0].plot(x, np.sin(3*x))

# Modify bottom-right plot
axes[1,1].set_title("Bottom--Right")
axes[1,1].plot(x, 1/(1+x))

# Depict illustration
plt.show()

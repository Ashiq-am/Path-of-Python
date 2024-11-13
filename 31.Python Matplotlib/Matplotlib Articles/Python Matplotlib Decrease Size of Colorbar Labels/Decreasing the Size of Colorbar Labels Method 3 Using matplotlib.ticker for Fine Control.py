import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# Sample data
data = np.random.rand(10, 10)

# Create plot
fig, ax = plt.subplots()
cax = ax.imshow(data, cmap='viridis')

# Add colorbar
cbar = fig.colorbar(cax, ax=ax)

# Create a custom formatter
formatter = ticker.FuncFormatter(lambda x, _: f'{x:.2f}')

# Set the formatter and label size
cbar.ax.yaxis.set_major_formatter(formatter)
cbar.ax.yaxis.set_tick_params(labelsize=6)  # Set label size to 6

plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Sample data: Sine wave
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)

# Setting custom limits for x and y axes
plt.xlim(0, 10)     # X-axis range from 0 to 10
plt.ylim(-1.5, 1.5) # Y-axis range from -1.5 to 1.5

# Adding titles and labels
plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show gridlines for better readability
plt.grid(True)

# Display the plot
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)

# Customizing ticks
plt.xticks(ticks=[0, 1, 2, 3], labels=['Zero', 'One', 'Two', 'Three'])
plt.yticks(fontsize=10)

plt.title('Sine Wave with Customized Ticks')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
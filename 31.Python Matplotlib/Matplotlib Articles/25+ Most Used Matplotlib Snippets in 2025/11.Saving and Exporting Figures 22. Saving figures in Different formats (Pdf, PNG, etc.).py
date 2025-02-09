import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create the plot
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Save the figure in multiple formats with custom settings
for fmt in ['png', 'pdf', 'svg']:
    plt.savefig(f'sine_wave.{fmt}', dpi=300, bbox_inches='tight')

plt.show()
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the data
for sample, measurements in data.items():
    x = np.full_like(measurements, sample)
    y = np.arange(len(measurements))
    z = measurements
    ax.plot(x, y, z, label=sample)

# Set the labels
ax.set_xlabel('Sample')
ax.set_ylabel('Wavelength Index')
ax.set_zlabel('Measurement')

# Add a legend
ax.legend()

# Show the plot
plt.show()

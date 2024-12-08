import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for non-GUI rendering
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6])
plt.savefig('plot.png')  # Save the plot as a PNG file
plt.close()  # Close the plot to free up memory
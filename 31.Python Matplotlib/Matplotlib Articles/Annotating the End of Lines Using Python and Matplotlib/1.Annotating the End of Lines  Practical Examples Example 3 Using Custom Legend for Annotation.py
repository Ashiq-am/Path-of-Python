import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [4, 9, 2, 8, 12]

# Create a line plot
plt.plot(x, y, label='Data Line')

# Add a custom legend for the last point
plt.plot(x[-1], y[-1], 'ro', label=f'End ({y[-1]})')
plt.legend()

plt.show()

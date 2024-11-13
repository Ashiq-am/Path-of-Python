import matplotlib.pyplot as plt

# Example data
x = [1, 2, 3, 4, 5]
y = [2.5, 1.5, 3.5, 2.0, 4.5]

# Plot
plt.plot(x, y, 'purple')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Example Plot')
plt.grid(True)

# Replace points with commas in tick labels
plt.xticks([tick for tick in plt.xticks()[0]], [
           str(tick).replace('.', ',') for tick in plt.xticks()[0]])
plt.yticks([tick for tick in plt.yticks()[0]], [
           str(tick).replace('.', ',') for tick in plt.yticks()[0]])

plt.show()

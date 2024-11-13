import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Example data
x = [1, 2, 3, 4, 5]
y = [2.5, 1.5, 3.5, 2.0, 4.5]

# Plot
plt.plot(x, y, 'gold')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Example Plot')
plt.grid(True)


def comma_formatter(x, pos):
    return str(x).replace('.', ',')


plt.gca().xaxis.set_major_formatter(FuncFormatter(comma_formatter))
plt.gca().yaxis.set_major_formatter(FuncFormatter(comma_formatter))

plt.show()

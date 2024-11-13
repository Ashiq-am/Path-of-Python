# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

# dummy data
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

# set graph color
plt.plot(x, y, 'green')

# to set title
plt.title("Plot with linewidth and linestyle")

# draws gridlines of grey color using given
# linewidth and linestyle
plt.grid(True, color = "grey", linewidth = "1.4", linestyle = "-.")

plt.show()

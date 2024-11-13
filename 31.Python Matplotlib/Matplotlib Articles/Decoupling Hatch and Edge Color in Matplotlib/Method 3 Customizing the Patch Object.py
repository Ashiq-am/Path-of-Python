import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4) + 1
y_red = [1, 3, 1, 4]
y_blue = [2, 2, 4, 1]

# Create the figure and axis
fig, ax = plt.subplots()

# Plot the bars with transparent face color
bars_red = ax.bar(x - 0.2, y_red, width=0.4, edgecolor='black', hatch='/', facecolor=(0, 0, 0, 0))
bars_blue = ax.bar(x + 0.2, y_blue, width=0.4, edgecolor='black', hatch='\\', facecolor=(0, 0, 0, 0))

# Customize the hatch color
for bar in bars_red:
    bar._hatch_color = (1.0, 0.0, 0.0, 1.0)  # Red hatch color

for bar in bars_blue:
    bar._hatch_color = (0.0, 0.0, 1.0, 1.0)  # Blue hatch color

plt.show()

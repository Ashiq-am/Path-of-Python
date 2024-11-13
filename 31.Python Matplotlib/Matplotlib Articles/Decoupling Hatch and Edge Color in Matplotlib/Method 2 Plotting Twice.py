import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [4, 5, 6]

# Create the figure and axis
fig, ax = plt.subplots()

# Plot the hatch
bars = ax.bar(x, y, color='white', edgecolor='red', hatch='/', linewidth=2)

# Plot the edge
bars = ax.bar(x, y, color='none', edgecolor='black', linewidth=2)

plt.show()

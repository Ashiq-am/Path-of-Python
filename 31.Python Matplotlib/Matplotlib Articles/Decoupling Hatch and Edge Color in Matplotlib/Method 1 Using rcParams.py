import matplotlib.pyplot as plt

# Set global hatch color
plt.rcParams['hatch.color'] = 'blue'

# Create a bar plot
fig, ax = plt.subplots()
bars = ax.bar([1, 2, 3], [3, 2, 5], color='white', edgecolor='black', hatch='/', linewidth=2)

plt.show()

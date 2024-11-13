import matplotlib.pyplot as plt

# Define subplots with different width ratios
fig, ax = plt.subplots(1, 2, gridspec_kw={'width_ratios': [3, 1]})
fig.tight_layout()

# Plot data in each subplot
ax[0].plot([1, 2, 3], [7, 13, 24], color='red')
ax[1].plot([1, 2, 3], [7, 13, 24], color='blue')
plt.show()

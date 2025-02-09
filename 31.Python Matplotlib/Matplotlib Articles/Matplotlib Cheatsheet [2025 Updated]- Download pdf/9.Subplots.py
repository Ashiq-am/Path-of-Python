# Create subplots
fig, axs = plt.subplots(2, 1, figsize=(6, 8))

# Plot on the first subplot
axs[0].plot(x, y, 'r-')
axs[0].set_title("Line Plot")

# Plot on the second subplot
axs[1].scatter(x, y, color='blue')
axs[1].set_title("Scatter Plot")

# Display the plots
plt.tight_layout()
plt.show()

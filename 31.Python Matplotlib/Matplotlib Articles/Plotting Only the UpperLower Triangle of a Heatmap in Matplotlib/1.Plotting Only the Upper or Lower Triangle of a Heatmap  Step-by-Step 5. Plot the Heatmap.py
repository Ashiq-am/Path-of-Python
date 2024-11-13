plt.figure(figsize=(8, 6))

# Plot lower triangle heatmap
plt.subplot(1, 2, 1)
plt.title("Lower Triangle Heatmap")
plt.imshow(masked_data_lower, interpolation='nearest', cmap='viridis')
plt.colorbar()

# Plot upper triangle heatmap
plt.subplot(1, 2, 2)
plt.title("Upper Triangle Heatmap")
plt.imshow(masked_data_upper, interpolation='nearest', cmap='viridis')
plt.colorbar()

plt.tight_layout()
plt.show()

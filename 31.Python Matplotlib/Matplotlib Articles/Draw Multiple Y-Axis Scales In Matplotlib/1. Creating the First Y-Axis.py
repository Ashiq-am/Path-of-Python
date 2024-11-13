# Create the first plot with the left Y-axis
fig, ax1 = plt.subplots(figsize=(8, 6))
# Plot the first dataset on the first Y-axis
ax1.plot(x, y1, 'b', label='y1 (sin(x))') # Shorthand 'b' for blue color

# Set labels and ticks for the first Y-axis
ax1.set_xlabel('X-axis')
ax1.set_ylabel('y1', color='b')
ax1.tick_params('y', colors='b')

# Display the plot
plt.title('Plotting the First Dataset on the First Y-Axis')
plt.show()

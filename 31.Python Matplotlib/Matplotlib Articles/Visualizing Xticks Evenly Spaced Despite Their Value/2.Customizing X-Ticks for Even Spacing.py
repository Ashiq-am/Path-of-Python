# Plot the data
plt.plot(x_values, y_values, marker='o')

# Set the number of x-ticks you want
num_xticks = len(x_values)

# Generate evenly spaced positions for x-ticks
evenly_spaced_xticks = np.arange(num_xticks)

# Set the x-ticks to the evenly spaced positions
plt.xticks(evenly_spaced_xticks, x_values)

plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Evenly Spaced X-Ticks')

plt.show()

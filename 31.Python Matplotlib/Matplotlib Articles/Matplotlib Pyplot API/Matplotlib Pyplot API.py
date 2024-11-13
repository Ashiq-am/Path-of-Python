import matplotlib.pyplot as plt

# Sample data
time = [0, 1, 2, 3, 4, 5]
temperature = [25, 27, 29, 31, 28, 26]

# Create a figure and axes
fig, ax = plt.subplots()

# Create a line plot
ax.plot(time, temperature, marker='o', linestyle='-',
		color='b', label='Temperature')

# Add labels and title
ax.set_xlabel('Time (hours)')
ax.set_ylabel('Temperature (°C)')
ax.set_title('Temperature Variation Over Time')

# Add a legend
ax.legend()

# Display the plot
plt.show()

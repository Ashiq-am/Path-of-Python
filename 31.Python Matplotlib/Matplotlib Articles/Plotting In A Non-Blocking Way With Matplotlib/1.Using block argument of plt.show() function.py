import numpy as np
import matplotlib.pyplot as plt

def main():
	# Set the axis limits for the plot
	plt.axis([-50, 50, 0, 10000])

	# Create an array of x values from -50 to 50
	x = np.arange(-50, 51)

	for power in range(1, 5):
		# Calculate y values for x^power
		y = [x_i ** power for x_i in x]

		# Plot the function
		plt.plot(x, y)

		# Redraw the plot
		plt.draw()

		# Pause for a short duration to allow visualization
		plt.pause(0.001)

		# Wait for user input to continue
		input("Press [Enter] to proceed to the next plot.")

if __name__ == '__main__':
	# Enable interactive mode for non-blocking plotting
	plt.ion()

	# Display the plot window in non-blocking mode
	plt.show(block=False)

	main()

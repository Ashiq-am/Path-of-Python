import matplotlib.pyplot as plt
import numpy as np

def plot_power(x, power):
	y = x ** power
	plt.plot(x, y)
	plt.title(f'Plot of x^{power}')
	plt.xlabel('X-axis')
	plt.ylabel('Y-axis')
	plt.draw()
	plt.pause(0.5)

def main():
	x = np.arange(-50, 51)
	powers = [1, 2, 3, 4]

	plt.axis([-50, 50, 0, 10000])
	plt.ion() # Turn on interactive mode

	for power in powers:
		plot_power(x, power)
		input(f'Press [Enter] to proceed to the next plot (x^{power}).')

	plt.ioff() # Turn off interactive mode
	plt.show()

if __name__ == '__main__':
	main()

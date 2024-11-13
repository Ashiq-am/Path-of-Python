import numpy as np
from matplotlib import pyplot as plt

def main():
	plt.axis([-10, 10, -10, 10]) # Adjust axis limits for various functions
	plt.ion()
	plt.show()

	x = np.arange(-10, 11)

	# Plot different mathematical functions
	for function_name in ["Linear", "Quadratic", "Cubic", "Square Root"]:
		if function_name == "Linear":
			y = x
		elif function_name == "Quadratic":
			y = x**2
		elif function_name == "Cubic":
			y = x**3
		elif function_name == "Square Root":
			y = np.sqrt(np.abs(x))

		plt.plot(x, y, label=function_name)
		plt.draw()
		plt.pause(0.001)
		input("Press [enter] to continue.")

if __name__ == '__main__':
	main()

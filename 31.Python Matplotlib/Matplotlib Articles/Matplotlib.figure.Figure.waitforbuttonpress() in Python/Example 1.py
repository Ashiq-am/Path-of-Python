# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

for ite in range(2):
	x = np.linspace(-2, 6, 100)
	y = (ite + 1)*x

	fig = plt.figure()
	ax = fig.subplots()
	ax.plot(x, y, '-b')

	fig.suptitle("""matplotlib.figure.Figure.waitforbuttonpress() 
	function Example\n\n""", fontweight ="bold")

	w = fig.waitforbuttonpress()
	print("Result after", ite, "click", w)

	fig.show()

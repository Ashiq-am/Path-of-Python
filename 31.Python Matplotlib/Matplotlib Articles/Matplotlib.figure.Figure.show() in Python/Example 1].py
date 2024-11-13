# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
x = np.arange(20) / 50
y = (x + 0.1)*2

val1 = [True, False] * 10
val2 = [False, True] * 10

plt.errorbar(x, y,
			xerr = 0.1,
			xlolims = True,
			label ='Line 1')
y = (x + 0.3)*3

plt.errorbar(x + 0.6, y,
			xerr = 0.1,
			xuplims = val1,
			xlolims = val2,
			label ='Line 2')

y = (x + 0.6)*4
plt.errorbar(x + 1.2, y,
			xerr = 0.1,
			xuplims = True,
			label ='Line 3')

plt.legend()

fig.suptitle("""matplotlib.figure.Figure.show() 
function Example\n\n""", fontweight ="bold")

fig.show()

# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt


x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

fig = plt.figure()
axs = fig.subplots()

axs.plot(x, y)

fig.subplots_adjust(bottom = 0.15)

fig.suptitle("""matplotlib.figure.Figure.subplots_adjust() 
function Example\n\n""", fontweight ="bold")

fig.show()

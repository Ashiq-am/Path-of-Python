# importing required properties
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 501)
y = np.sin(x)

figtext_args = (0.5, 0,
				"figtext using args and kwargs")

figtext_kwargs = dict(horizontalalignment ="center",
					fontsize = 14, color ="green",
					style ="italic", wrap = True)

plt.plot(x, y)
plt.figtext(*figtext_args, **figtext_kwargs)
plt.show()

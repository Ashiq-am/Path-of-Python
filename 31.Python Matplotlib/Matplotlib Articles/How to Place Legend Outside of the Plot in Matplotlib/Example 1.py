# importing packages
import numpy as np
import matplotlib.pyplot as plt

# create data
x = np.linspace(-20, 20, 1000)

# plot the graphs
plt.plot(x,np.sin(x))
plt.plot(x,np.cos(x))

# add legends and set its box position
plt.legend(["Sine","Cosine"],
		bbox_to_anchor = (1.05, 0.6))

plt.show()

# importing various package
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# making Time series
spacing = np.linspace(-5 * np.pi, 5 * np.pi, num=100)
s = pd.Series(0.7 * np.random.rand(100) + 0.3 * np.sin(spacing))

# Creating Autocorrelation plot
x = pd.plotting.autocorrelation_plot(s)

# ploting the Curve
x.plot()

# Display
plt.show()

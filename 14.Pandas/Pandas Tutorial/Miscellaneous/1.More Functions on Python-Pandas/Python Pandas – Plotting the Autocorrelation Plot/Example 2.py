# importing various package
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# making Time series
data = np.array([12.0, 24.0, 7., 20.0,
				7.0, 22.0, 18.0,22.0,
				6.0, 7.0, 20.0, 13.0,
				8.0, 5.0, 8])

# Creating Autocorrelation plot
x = pd.plotting.autocorrelation_plot(data)

# ploting the Curve
x.plot()

# Display
plt.show()

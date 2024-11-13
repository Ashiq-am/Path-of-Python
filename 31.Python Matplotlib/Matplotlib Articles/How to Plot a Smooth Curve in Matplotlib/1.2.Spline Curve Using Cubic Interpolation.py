import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Dataset
x=np.array([1, 2, 3, 4, 5, 6, 7, 8])
y=np.array([20, 30, 5, 12, 39, 48, 50, 3])

cubic_interploation_model = interp1d(x, y, kind = "cubic")

# Plotting the Graph
X_=np.linspace(x.min(), x.max(), 500)
Y_=cubic_interploation_model(X_)

plt.plot(X_, Y_)
plt.title("Plot Smooth Curve Using the scipy.interpolate.interp1d Class")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

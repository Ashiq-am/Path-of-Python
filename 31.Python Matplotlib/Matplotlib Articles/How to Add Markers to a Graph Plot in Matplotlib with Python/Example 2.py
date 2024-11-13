# importing packages
import matplotlib.pyplot as plt

# create data
from plotly.figure_factory import np

t = np.arange(0., 5., 0.2)

# plot with marker
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

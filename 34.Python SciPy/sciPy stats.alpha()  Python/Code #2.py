# Python code to demonstrate scipy.alpha()
import numpy as np
import matplotlib.pyplot as plt

# getting distribution using linspace()
distribution = np.linspace(0, np.minimum(rv.dist.b, 3))
plot = plt.plot(distribution, rv.pdf(distribution))

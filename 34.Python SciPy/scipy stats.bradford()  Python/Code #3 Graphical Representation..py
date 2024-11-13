import numpy as np
import matplotlib.pyplot as plt

distribution = np.linspace(0, np.maximum(rv.dist.b, 5))
print ("Distribution : \n", distribution)

plot = plt.plot(distribution, rv.pdf(distribution))

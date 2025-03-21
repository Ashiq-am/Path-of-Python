# libraries
import numpy as np
import matplotlib.pyplot as plt

distribution = np.linspace(0, np.minimum(rv.dist.b, 3))
print ("Distribution : \n", distribution)

plot = plt.plot(distribution, rv.pdf(distribution))

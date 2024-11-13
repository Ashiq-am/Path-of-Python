# import packages
import matplotlib.pyplot as plt
import numpy as np

# slope and intercepts
a1, b1 = (1/4), 1.0
a2, b2 = (3/4), 0.0

# The numpy.linspace() function returns
# number spaces evenly w.r.t interval
l = np.linspace(-6, 6, 100)

# use to create new figure
plt.figure(figsize=(8, 8))

# plotting
plt.xlim(0, 6)
plt.ylim(0, 6)
plt.title('Plot an angle using Python')
plt.plot(l, l*a1+b1)
plt.plot(l, l*a2+b2)
plt.show()

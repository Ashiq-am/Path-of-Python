# import packages
import matplotlib.pyplot as plt
import numpy as np

# return values between 0 and 10 with
# even space of 0.1
x = np.arange(0, 10, 0.1)

# generate value of sine function for
# given x values
y = np.sin(x)

# plot graph of sine function
plt.plot(y, color='blue')

# Set the range of x-axis
plt.xlim(0, 32)
# Set the range of y-axis
plt.ylim(0, 1)

# display plot
plt.show()

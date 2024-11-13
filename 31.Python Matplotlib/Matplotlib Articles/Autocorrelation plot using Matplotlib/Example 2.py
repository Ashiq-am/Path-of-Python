# Importing the libraries.
import matplotlib.pyplot as plt
import numpy as np

# Setting up the rondom seed for
# fixing the random state.
np.random.seed(42)

# Creating some random data.
data = np.random.randn(25)

# Adding plot title.
plt.title("Autocorrelation Plot")

# Providing x-axis name.
plt.xlabel("Lags")

# Plotting the Autocorreleation plot.
plt.acorr(data, maxlags=20)

# Displaying the plot.
print("The Autocorreleation plot for the data is:")
plt.grid(True)

plt.show()

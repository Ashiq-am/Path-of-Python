# Importing the libraries.
import matplotlib.pyplot as plt
import numpy as np

# Data for which we plot Autocorreleation.
data = np.array([12.0, 24.0, 7., 20.0,
                 7.0, 22.0, 18.0, 22.0,
                 6.0, 7.0, 20.0, 13.0,
                 8.0, 5.0, 8])

# Adding plot title.
plt.title("Autocorrelation Plot")

# Providing x-axis name.
plt.xlabel("Lags")

# Plotting the Autocorreleation plot.
plt.acorr(data, maxlags=10)

# Displaying the plot.
print("The Autocorreleation plot for the data is:")
plt.grid(True)

plt.show()

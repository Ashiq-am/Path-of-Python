# Code to change the interval of ticks of axes using xticks() and yticks()

# Importing libraries
import matplotlib.pyplot as plt
import numpy as np

#Creating x-value and y-value of data
x = [5, 10, 15, 20]
y = [10, 20, 30, 40]

# Plotting the data
plt.plot(x, y)

# Setting the interval of ticks of x-axis to 5.
listOf_Xticks = np.arange(0, 25, 5)
plt.xticks(listOf_Xticks)

# Setting the interval of ticks of y-axis to 10.
listOf_Yticks = np.arange(0, 50, 10)
plt.yticks(listOf_Yticks)

# Giving title to the plot
plt.title('matplotlib.pyplot.xticks() and matplotlib.pyplot.yticks() Example')

plt.show()

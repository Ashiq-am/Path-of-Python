# importing the modules
from scipy import random
import numpy as np
import matplotlib.pyplot as plt

# limits of integration
a = 0
b = 1
N = 1000


# function to calculate x^2 of a particular value
# of x
def f(x):
    return x ** 2


# list to store all the values for plotting
plt_vals = []

# we iterate through all the values to generate
# multiple results and show whose intensity is
# the most.
for i in range(N):

    # array of zeros of length N
    ar = np.zeros(N)

    # iterating over each Value of ar and filling
    # it with a randome value between the limits a
    # and b
    for i in range(len(ar)):
        ar[i] = random.uniform(a, b)

    # variable to store sum of the functions of
    # different values of x
    integral = 0.0

    # iterates and sums up values of different functions
    # of x
    for i in ar:
        integral += f(i)

    # we get the answer by the formula derived abobe
    ans = (b - a) / float(N) * integral

    # appends the solution to a list for plotting the
    # graph
    plt_vals.append(ans)

# details of the plot to be genrated
# sets the title of the plot
plt.title("Distributions of areas calculated")

# 3 parameters (array on which histogram needs
# to be made, bins, seperators colour between
# the beams)
plt.hist(plt_vals, bins=30, ec="black")

# sets the label of the x-axis of the plot
plt.xlabel("Areas")
plt.show()  # shows the plot

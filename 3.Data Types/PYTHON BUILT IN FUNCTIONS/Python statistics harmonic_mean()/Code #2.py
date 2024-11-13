# Python3 program to demonstrate harmonic_mean()
# function from the statistics module

# Importing the statistics module
from statistics import harmonic_mean

# Importing fractions module as fr
from fractions import Fraction as fr

# tuple of positive integer numbers
data1 = (2, 3, 4, 5, 7, 9, 11)

# tuple of a set of floating point values
data2 = (2.4, 5.1, 6.7, 8.9)

# tuple of a set of fractional numbers
data3 = (fr(1, 2), fr(44, 12), fr(10, 3), fr(2, 3))

# dictionary of a set of values
# Only the keys are taken in
# consideration by harmonic_mean()
data4 = {1: "one", 2: "two", 3: "three"}

# Printing the harmonic mean of above datsets
print("Harmonic Mean of data set 1 is % s"
      % (harmonic_mean(data1)))

print("Harmonic Mean of data set 2 is % s"
      % (harmonic_mean(data2)))

print("Harmonic Mean of data set 3 is % s"
      % (harmonic_mean(data3)))

print("Harmonic Mean of data set 4 is % s"
      % (harmonic_mean(data4)))

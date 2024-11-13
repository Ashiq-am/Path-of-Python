# Python Program to explain math.perm() method

# Importing math module
import math

# When k > n
# math.perm(n, k) returns 0.
n = 3
k = 5

# Get the number of ways to choose
# k items from n items without
# repetition and with order
nPk = math.perm(n, k)
print(nPk)

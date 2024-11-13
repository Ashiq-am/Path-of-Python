# Python Program to explain math.comb() method

# Importing math module
import math

# When k > n
# math.comb(n, k) returns 0.
n = 3
k = 5

# Get the number of ways to choose
# k items from n items without
# repetition and without order
nCk = math.comb(n, k)
print(nCk)

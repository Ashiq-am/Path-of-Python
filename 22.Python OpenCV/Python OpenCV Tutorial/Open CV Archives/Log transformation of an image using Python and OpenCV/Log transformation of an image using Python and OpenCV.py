import numpy as np

# input a number as integer
a = int(input())

print("Natural log value of the input number is", np.log(a))

# If you want base of log to be set to 2
print("Log value of the number with base 2 is", np.log2(a))

# If you want base of log to be set to 10
print("Log value of the number with base 10 is", np.log10(a))

# importing the module
import numpy as np

# taking thecelsius input
inp = [0, 12, 45.21, 34, 99.91]

# arange will not directly
# convert into numpy array
cel = np.arange(5)

# the above code
# will give o/p as
# cel = [0, 1, 2, 3, 4]
cel = [i for i in inp]
# thus the input(inp)
# is stored in cel
# using list comprehension

print(f"Celsius {cel}")

# applying formulae
# using list comprehension
feh = [(9 * i / 5 + 32) for i in cel]

# printing results
print(f"Fahrenheit {feh}")

import numpy as np

# Defining a positive infinite integer
a = np.inf

# Defining a negative infinite integer
b = -np.inf

# Define a finite + ve integer
c = 300

# Define a finite -ve integer
d = -300


# helper function to make comparisions
def compare(x, y):
    if x > y:
        print("True")
    else:
        print("False")


compare(a, b)
compare(a, c)
compare(a, d)
compare(b, c)
compare(b, d)

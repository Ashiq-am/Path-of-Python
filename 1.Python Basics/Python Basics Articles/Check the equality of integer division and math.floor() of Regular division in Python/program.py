# Python program to demonstrate
# equality of integer division and
# math.floor


import math

# First case: Take x smaller
# than 2 ^ 53 .
x = 269
y = 3
if (x // y) == math.floor(x / y):
    print("Equal Output")

else:
    print("Not Equal Output")

# Second case: Take x larger
# than 2 ^ 53.
x = 269792703866060742
y = 3
if (x // y) == math.floor(x / y):
    print("Equal Output")

else:
    print("Not Equal Output")

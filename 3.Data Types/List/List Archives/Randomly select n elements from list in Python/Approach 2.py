# importing random module
import random

# declaring list
list = [2, 2, 4, 6, 6, 8]

# initializing the value of n
n = 4

# traversing and printing random elements
for i in range(n):
    # end = " " so that we get output in single line
    print(random.choice(list), end=" ")

# Python3 program to demonstrate the
# error of sample() function.
import random

list1 = [1, 2, 3, 4]

# exception raised
print(random.sample(list1, 5))

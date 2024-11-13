# Python3 code to demonstrate
# to generate random number list
# using list comprehension + randrange()
import random

# using list comprehension + randrange()
# to generate random number list
res = [random.randrange(1, 50, 1) for i in range(7)]

# printing result
print ("Random number list is : " + str(res))

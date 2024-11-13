# Python3 code to demonstrate
# Random Numbers Summation
# using list comprehension + randrange() + sum()
import random

# using list comprehension + randrange() + sum()
# Random Numbers Summation
res = sum([random.randrange(1, 50, 1) for i in range(7)])

# printing result
print ("Random number summation list is : " + str(res))

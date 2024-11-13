# Python3 code to demonstrate
# Random Numbers Summation
# using random.sample() + sum()
import random

# using random.sample() + sum()
# Random Numbers Summation
res = sum(random.sample(range(1, 50), 7))

# printing result
print ("Random number summation list is : " + str(res))

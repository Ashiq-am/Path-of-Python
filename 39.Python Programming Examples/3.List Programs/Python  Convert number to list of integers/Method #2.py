# Python3 code to demonstrate
# conversion of number to list of integers
# using map()

# initializing number
num = 2019

# printing number
print ("The original number is " + str(num))

# using map()
# to convert number to list of integers
res = list(map(int, str(num)))

# printing result
print ("The list from number is " + str(res))

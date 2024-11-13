# initializing string
test_str = '5x6, 9x10, 7x8'

# printing original string
print("The original string is : " + str(test_str))

# using replace() to create eval friendly string
temp = test_str.replace(',', '+').replace('x', '*')

# using eval() to get the required result
res = eval(temp)

# printing result
print("The computed summation of products : " + str(res))

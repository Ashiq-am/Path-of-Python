# Python3 code to demonstrate
# to generate successive difference list
# using map() + operator.sub
import operator

# initializing list
test_list = [1, 4, 5, 3, 6]

# printing original list
print ("The original list is : " + str(test_list))

# using map() + operator.sub
# generate successive difference list
res = list(map(operator.sub, test_list[1:], test_list[:-1]))

# printing result
print ("The computed successive difference list is : " + str(res))

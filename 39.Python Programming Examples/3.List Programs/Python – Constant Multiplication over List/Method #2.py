# Python3 code to demonstrate
# Constant Multiplication over List
# using map() + operator.mul
import operator

# initializing list
test_list = [4, 5, 6, 3, 9]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K list
K_list = [4] * len(test_list)

# using map() + operator.mul
# Constant Multiplication over List
res = list(map(operator.mul, test_list, K_list))

# printing result
print ("The list after constant multiplication : " + str(res))

# Python3 code to demonstrate
# Exponentiation by K in list
# using map() + operator.pow
import operator

# initializing list
test_list = [4, 5, 6, 3, 9]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K list
K_list = [4] * len(test_list)

# using map() + operator.pow
# Exponentiation by K in list
res = list(map(operator.pow, test_list, K_list))

# printing result
print ("The list after constant exponentiation : " + str(res))

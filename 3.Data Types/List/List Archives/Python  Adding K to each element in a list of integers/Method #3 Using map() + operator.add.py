# Python3 code to demonstrate
# adding K to each element
# using map() + operator.add
import operator

# initializing list
test_list = [4, 5, 6, 3, 9]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K list
K_list = [4] * len(test_list)

# using map() + operator.add
# adding K to each element
res = list(map(operator.add, test_list, K_list))

# printing result
print ("The list after adding K to each element : " + str(res))

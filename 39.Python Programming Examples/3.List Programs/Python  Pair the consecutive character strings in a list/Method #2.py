# Python3 code to demonstrate working of
# Consecutive element pairing in list
# using map() + concat
import operator

# initialize list
test_list = ["G", "F", "G", "I", "S", "B", "E", "S", "T"]

# printing original list
print("The original list : " + str(test_list))

# Consecutive element pairing in list
# using map() + concat
res = list(map(operator.concat, test_list[:-1], test_list[1:]))

# printing result
print("List after Consecutive concatenation is : " + str(res))

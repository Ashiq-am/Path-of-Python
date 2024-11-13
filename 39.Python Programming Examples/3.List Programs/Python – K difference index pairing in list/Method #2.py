# Python3 code to demonstrate working of
# K difference index pairing in list
# using map() + concat
import operator

# initialize list
test_list = ["G", "F", "G", "I", "S", "B", "E", "S", "T"]

# printing original list
print("The original list : " + str(test_list))

# initialize K
K = 3

# K difference index pairing in list
# using map() + concat
res = list(map(operator.concat, test_list[:-1], test_list[K:]))

# printing result
print("List after K difference concatenation is : " + str(res))

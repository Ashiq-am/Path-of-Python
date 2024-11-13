# Python3 code to demonstrate
# grouping like elements as list
# using collections.Counter()
import collections

# initializing list
test_list = [1, 3, 4, 2, 1, 3, 4, 2, 3, 4, 1]

# printing original list
print("The original list : " + str(test_list))

# using collections.Counter()
# grouping like elements as list
temp = collections.Counter(test_list)
res = [[i] * j for i, j in temp.items()]

# print result
print("The elements after grouping are : " + str(res))

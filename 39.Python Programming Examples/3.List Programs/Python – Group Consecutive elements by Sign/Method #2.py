# Python3 code to demonstrate working of
# Group Consecutive elements by Sign
# Using groupby() + list comprehension
import itertools

# initializing list
test_list = [-2, 3, 4, 5, 6, -3]

# printing original list
print("The original list is : " + str(test_list))

# grouped using groupby()
res = [list(ele) for idx, ele in itertools.groupby(test_list, lambda a: a > 0)]

# printing result
print("Elements after sign grouping : " + str(res))

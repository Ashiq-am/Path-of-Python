# Python3 code to demonstrate working of
# Relative Size Ordering
# Using sorted() + set() + index() + list comprehension

# initializing list
test_list = [8, 3, 5, 8, 1, 5, 4]

# printing original list
print("The original list is : " + str(test_list))

# getting order
ord_dict = list(set(test_list))

# mapping index
res = [ord_dict.index(ele) for ele in test_list]

# printing result
print("Relative size ordered list : " + str(res))

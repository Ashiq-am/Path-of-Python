# Python3 code to demonstrate working of
# Remove particular element from tuple list
# using list comprehension

# initialize list
test_list = [(5, 6, 7), (7, 2, 4, 6), (6, 6, 7), (6, 10, 8)]

# printing original list
print("The original list is : " + str(test_list))

# declaring remove element
N = 6

# Remove particular element from tuple list
# using list comprehension
res = [tuple(ele for ele in sub if ele != N) for sub in test_list]

# printing result
print("The Tuple List after removal of element : " + str(res))

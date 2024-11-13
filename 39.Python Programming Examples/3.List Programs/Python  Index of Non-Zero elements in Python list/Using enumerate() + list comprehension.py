# Python3 code to demonstrate working of
# Index of Non-Zero elements in Python list
# using list comprehension + enumerate()

# initialize list
test_list = [6, 7, 0, 1, 0, 2, 0, 12]

# printing original list
print("The original list is : " + str(test_list))

# Index of Non-Zero elements in Python list
# using list comprehension + enumerate()
res = [idx for idx, val in enumerate(test_list) if val != 0]

# printing result
print("Indices of Non-Zero elements : " + str(res))

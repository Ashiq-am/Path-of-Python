# Python3 code to demonstrate
# Atmost K element indices
# using list comprehension + enumerate()

# initializing list
test_list = [12, 11, 7, 15, 8, 18]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + enumerate()
# Atmost K element indices
res = [idx for idx, val in enumerate(test_list) if val <= 11]

# print result
print("The list of indices at most 11 : " + str(res))

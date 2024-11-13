# Python3 code to demonstrate working of
# Index Value Product Sum
# Using loop + enumerate()

# initializing list
test_list = [5, 3, 4, 9, 1, 2]

# printing original list
print("The original list is : " + str(test_list))

# one liner to solve problem using list comprehension
res = sum([(idx + 1) * ele for idx, ele in enumerate(test_list)])

# printing result
print("The computed sum : " + str(res))

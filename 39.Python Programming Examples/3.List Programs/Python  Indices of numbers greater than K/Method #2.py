# Python3 code to demonstrate
# index of matching element
# using list comprehension + enumerate()

# initializing list
test_list = [12, 10, 18, 15, 8, 18]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + enumerate()
# index of matching element
res = [idx for idx, val in enumerate(test_list) if val > 10]

# print result
print("The list of indices greater than 10 : " + str(res))

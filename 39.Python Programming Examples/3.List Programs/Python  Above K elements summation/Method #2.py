# Python3 code to demonstrate
# Above K elements summation
# using list comprehension + sum()

# initializing list
test_list = [12, 10, 18, 15, 8, 18]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + sum()
# index of matching element
res = sum(ele for ele in test_list if ele > 10)

# print result
print("The summation of elements greater than 10 : " + str(res))

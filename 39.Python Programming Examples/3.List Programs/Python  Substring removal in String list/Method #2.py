# Python3 code to demonstrate
# Substring removal in String list
# using list comprehension + map() + lambda

# initializing list
test_list = ['4', 'kg', 'butter', 'for', '40', 'bucks']

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + map() + lambda
# Substring removal in String list
res = list(map(lambda st: str.replace(st, "4", ""), test_list))

# print result
print("The list after substring removal : " + str(res))

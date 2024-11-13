# Python3 code to demonstrate
# Replace substring in list of strings
# using list comprehension + map() + lambda

# initializing list
test_list = ['4', 'kg', 'butter', 'for', '40', 'bucks']

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + map() + lambda
# Replace substring in list of strings
res = list(map(lambda st: str.replace(st, "4", "1"), test_list))

# print result
print("The list after substring replacement : " + str(res))

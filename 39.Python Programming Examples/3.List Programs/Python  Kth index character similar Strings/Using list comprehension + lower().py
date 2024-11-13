# Python3 code to demonstrate
# Kth index character similar Strings
# using list comprehension + lower()

# initializing list
test_list = ['Akash', 'Nikhil', 'Manjeet', 'akshat']

# initializing check letter
check = 'k'

# initializing K
K = 2

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + lower()
# Kth index character similar Strings
res = [idx for idx in test_list if idx[K - 1].lower() == check.lower()]

# print result
print("The list of matching Kth letter : " + str(res))

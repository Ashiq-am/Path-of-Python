# Python3 code to demonstrate
# Words starting with specific letter
# using list comprehension + startswith() + lower()

# initializing list
test_list = ['Akash', 'Nikhil', 'Manjeet', 'akshat']

# initializing check letter
check = 'A'

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + startswith() + lower()
# Words starting with specific letter
res = [idx for idx in test_list if idx.lower().startswith(check.lower())]

# print result
print("The list of matching first letter : " + str(res))

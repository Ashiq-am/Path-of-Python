# Python3 code to demonstrate
# Words with Particular Rear letter
# using list comprehension + endswith() + lower()

# initializing list
test_list = ['Akash', 'Nikhil', 'Manjeet', 'akshat']

# initializing check letter
check = 'T'

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + endswith() + lower()
# Words with Particular Rear letter
res = [idx for idx in test_list if idx.lower().endswith(check.lower())]

# print result
print("The list of matching last letter : " + str(res))

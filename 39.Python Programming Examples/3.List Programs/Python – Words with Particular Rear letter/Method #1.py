# Python3 code to demonstrate
# Words with Particular Rear letter
# using list comprehension + lower()

# initializing list
test_list = ['Akash', 'Nikhil', 'Manjeet', 'akshat']

# initializing check letter
check = 'T'

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + lower()
# Words with Particular Rear letter
res = [idx for idx in test_list if idx[len(idx) - 1].lower() == check.lower()]

# print result
print("The list of matching last letter : " + str(res))

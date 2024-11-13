# Python3 code to demonstrate
# Merge adjacent Digit characters
# list comprehension + "*" operator

# initializing list
test_list = ['Geeks', 'for', 'Geeks', '2', '5']

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + "*" operator
# Merge adjacent Digit characters
res = [''.join([i for i in test_list if not i.isalpha()]), *[j for j in test_list if j.isalpha()]]

# print result
print("The joined adjacent word list(ignoring alphabets) : " + str(res))

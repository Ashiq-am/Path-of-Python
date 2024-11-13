# Python3 code to demonstrate working of
# Remove multiple empty spaces from string List
# Using list comprehension + strip()

# initializing list
test_list = ['gfg', ' ', ' ', 'is', '		 ', 'best']

# printing original list
print("The original list is : " + str(test_list))

# Remove multiple empty spaces from string List
# Using list comprehension + strip()
res = [ele for ele in test_list if ele.strip()]

# printing result
print("List after filtering non-empty strings : " + str(res))

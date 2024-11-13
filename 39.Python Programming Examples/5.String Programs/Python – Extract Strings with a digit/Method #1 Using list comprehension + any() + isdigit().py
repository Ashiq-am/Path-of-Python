# Python3 code to demonstrate working of
# Extract Strings with a digit
# Using list comprehension + any() + isdigit()

# initializing list
test_list = ['gf4g', 'is', 'best', '4', 'gee1ks']

# printing original list
print("The original list is : " + str(test_list))

# checking if string contain any string using any()
res = [sub for sub in test_list if any(ele for ele in sub if ele.isdigit())]

# printing result
print("Strings with any digit : " + str(res))

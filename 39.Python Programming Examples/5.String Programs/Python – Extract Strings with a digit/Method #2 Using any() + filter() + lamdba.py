# Python3 code to demonstrate working of
# Extract Strings with a digit
# Using any() + filter() + lamdba

# initializing list
test_list = ['gf4g', 'is', 'best', '4', 'gee1ks']

# printing original list
print("The original list is : " + str(test_list))

# checking if string contain any string using any()
# filter() used to filter strings with digits
res = list(filter(lambda sub: any(
	ele for ele in sub if ele.isdigit()), test_list))

# printing result
print("Strings with any digit : " + str(res))

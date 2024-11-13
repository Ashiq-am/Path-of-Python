# Python3 code to demonstrate working of
# Remove trailing / leading special characters from strings list
# Using map() + str.strip()

# initializing list
test_list = ['\rgfg\t\n', 'is\n', '\t\tbest\r']

# printing list
print("The original list : " + str(test_list))

# Remove trailing / leading special characters from strings list
# Using map() + str.strip()
res = list(map(str.strip, test_list))

# Printing result
print("List after removal of special characters : " + str(res))

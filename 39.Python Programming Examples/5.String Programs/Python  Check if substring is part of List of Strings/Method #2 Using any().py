# Python3 code to demonstrate working of
# Check if substring is part of List of Strings
# Using any()

# initializing list
test_list = ['GeeksforGeeks', 'is', 'Best']

# test string
check_str = "for"

# printing original string
print("The original string is : " + str(test_list))

# Using any()
# Check if substring is part of List of Strings
res = any(check_str in sub for sub in test_list)

# printing result
print("Is check string part of any input list string : " + str(res))

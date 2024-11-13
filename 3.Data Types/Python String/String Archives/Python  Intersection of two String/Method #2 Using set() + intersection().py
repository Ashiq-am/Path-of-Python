# Python3 code to demonstrate
# string intersection
# using set() + intersection()

# initializing strings
test_str1 = 'GeeksforGeeks'
test_str2 = 'Codefreaks'

# using set() + intersection() to
# get string intersection
res = set(test_str1).intersection(test_str2)

# printing intersection
print("String intersection is : " + str(res))

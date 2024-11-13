# Python 3 code to demonstrate
# String uncommon characters
# using join()

# initializing strings
test_str1 = 'GeeksforGeeks'
test_str2 = 'Codefreaks'

# Printing initial strings
print("The original string 1 is : " + test_str1)
print("The original string 2 is : " + test_str2)

# using join() to
# String uncommon characters
res = ''.join(sorted(set(test_str1) ^ set(test_str2)))

# printing symmetric_difference
print("The string uncommon elements are : " + str(res))

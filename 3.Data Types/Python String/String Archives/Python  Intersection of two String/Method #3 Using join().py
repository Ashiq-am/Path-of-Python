# Python3 code to demonstrate
# string intersection
# using join()

# initializing strings
test_str1 = 'GeeksforGeeks'
test_str2 = 'Codefreaks'

# using join() to
# get string intersection
res = ''.join(sorted(set(test_str1) &
                     set(test_str2), key=test_str1.index))

# printing intersection
print("String intersection is : " + str(res))

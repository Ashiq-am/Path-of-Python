# Python3 code to demonstrate
# string intersection
# using naive method

# initializing strings
test_str1 = 'GeeksforGeeks'
test_str2 = 'Codefreaks'

# using naive method to
# get string intersection
res = ""
for i in test_str1:
    if i in test_str2 and not i in res:
        res += i

    # printing intersection
print("String intersection is : " + res)

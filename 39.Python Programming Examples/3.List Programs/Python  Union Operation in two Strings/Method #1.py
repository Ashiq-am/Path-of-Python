# Python 3 code to demonstrate
# Union Operation in two Strings
# using naive method

# initializing strings
test_str1 = 'GeeksforGeeks'
test_str2 = 'Codefreaks'

# Printing initial strings
print("The original string 1 is : " + test_str1)
print("The original string 2 is : " + test_str2)

# using naive method to
# Union Operation in two Strings
res = ""
temp = test_str1
for i in test_str2:
    if i not in temp:
        test_str1 += i

# printing result
print("The string union is : " + test_str1)

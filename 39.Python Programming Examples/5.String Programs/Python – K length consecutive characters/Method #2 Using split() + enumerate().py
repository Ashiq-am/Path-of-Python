# Python3 code to demonstrate working of
# K length consecutive characters
# Using split() + enumerate()

# initializing string
test_str = 'geekforgeeekssss is bbbbest forrrr geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 4

res = []
for idx, ele in enumerate(test_str):

    # creating equi string
    substr = ele * K

    # checking if equal to actual string
    if test_str[idx: idx + K] == substr:
        res.append(substr)

    # printing result
print("The K length similar characters : " + str(list(set(res))))

# Python3 code to demonstrate working of
# Extract indices of Present, Non Index matching Strings
# using loop + enumerate()

# initializing strings
test_str1 = 'apple'
test_str2 = 'pineapple'

# printing original Strings
print("The original string 1 is : " + str(test_str1))
print("The original string 2 is : " + str(test_str2))

# the replaced result
res = []
for idx, val in enumerate(test_str1):

    # if present in string 2
    if val in test_str2:

        # if not present at same index
        if test_str2[idx] != val:
            res.append(idx)

        # printing result
print("The extracted indices : " + str(res))

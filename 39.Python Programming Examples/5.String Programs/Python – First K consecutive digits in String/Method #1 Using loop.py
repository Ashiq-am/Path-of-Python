# Python3 code to demonstrate working of
# First K consecutive digits in String
# Using loop

# initializing string
test_str = "geeks5geeks43isbest"

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 2

# using loop to run through characters
res = ""
for idx in range(len(test_str) - K + 1):
    is_num = True

    # check for valid number of consecutives
    for j in range(K):
        is_num = is_num & test_str[idx + j].isdigit()

    # extracting numbers
    if is_num:
        res = ""
        for j in range(K):
            res += test_str[idx + j]

        # printing result
print("Required character digits : " + str(res))

# Python3 code to demonstrate working of
# Remove index ranges from String
# Using loop

# initializing strings
test_str1 = 'geeksforgeeks is best for geeks'

# printing original string
print("The original string 1 is : " + str(test_str1))

# initializing ranges list
range_list = [(3, 6), (7, 10), (14, 17)]

res = ""

for idx, chr in enumerate(test_str1):
    for strt_idx, end_idx in range_list:

        # checking for ranges and appending
        if strt_idx <= idx + 1 <= end_idx:
            break
    else:
        res += chr

# printing result
print("The reconstructed string : " + str(res))

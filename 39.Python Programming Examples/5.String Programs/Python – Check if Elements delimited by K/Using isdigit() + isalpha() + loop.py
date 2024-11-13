# Python3 code to demonstrate working of
# Check if Elements delimited by K
# Using isdigit() + isalpha() + loop

# initializing string
test_str = '72@45@geeks@best'

# printing original string
print("The original string is : " + str(test_str))

# initializing splt_chr
K = "@"

res = True

# splitting elements
temp = test_str.split(K)

for ele in temp:

    # checking for non-alpha or non-digit
    if len(ele) > 1 and not ele.isdigit() and not ele.isalpha():
        res = False
        break

# printing result
print("Are all delimited by K : " + str(res))

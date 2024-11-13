# Python3 code to demonstrate working of
# Append according to Kth character
# Using loop

# initializing lists
test_list = ["geeksforgeeks", "best", "for", "geeks"]

# printing string
print("The original list : " + str(test_list))

# initializing K
K = 2

# initializing N
N = 'e'

# initializing i, j
i, j = "**", "##"

res = []
for sub in test_list:

    # checking for Kth index to be N
    if sub[K] == N:
        res.append(sub + i)
    else:
        res.append(sub + j)

    # printing results
print("The resultant List : " + str(res))

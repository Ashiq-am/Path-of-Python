# Python3 code to demonstrate working of
# Length Conditional Concatenation
# Using loop + len()

# initializing lists
test_list = ["Gfg", 'is', "Best", 'for', 'CS', 'Everything']

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 2

# loop to run through all the elements
res = ''
for ele in test_list:

    # using len() to check for length
    if len(ele) > 2:
        res += ele

    # printing result
print("String after Concatenation : " + str(res))

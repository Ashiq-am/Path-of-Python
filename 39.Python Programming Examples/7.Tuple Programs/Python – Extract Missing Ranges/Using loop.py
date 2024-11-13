# Python3 code to demonstrate working of
# Extract Missing Ranges
# Using loop

# initializing lists
test_list = [(6, 9), (15, 34), (48, 70)]

# printing original list
print("The original list is : " + str(test_list))

# initializing start val
strt_val = 2

# initializing stop val
stop_val = 100

# Using loop
res = []
for sub in test_list:

    # checking for start range
    if sub[0] > strt_val:
        res.append((strt_val, sub[0]))
        strt_val = sub[1]

    # checking for end range
    if strt_val < stop_val:
        res.append((strt_val, stop_val))

    # printing result
print("Missing range tuples : " + str(res))

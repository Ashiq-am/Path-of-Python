# Python3 code to demonstrate working of
# Test for desired String Lengths
# Using loop

# initializing string list
test_list = ["Gfg", 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list is : " + str(test_list))

# initializing Lengths list
len_list = [3, 2, 4, 3, 5]

res = True
for idx in range(len(test_list)):

    # checking for string lengths
    if len(test_list[idx]) != len_list[idx]:
        res = False
        break

# printing result
print("Are all strings of required lengths : " + str(res))

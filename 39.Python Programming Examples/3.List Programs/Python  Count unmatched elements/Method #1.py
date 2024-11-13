# Python 3 code to demonstrate
# Count unmatched elements
# using loop

# initializing list
test_list = [3, 5, 1, 6, 7, 9]

# printing original list
print("The original list is : " + str(test_list))

# using loop
# Count unmatched elements
# checks for odd
res = 0
for ele in test_list:
    if not ele % 2 != 0:
        res = res + 1

# printing result
print("The number of non-odd elements: " + str(res))
